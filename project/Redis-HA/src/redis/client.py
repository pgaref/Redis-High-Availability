__author__ = 'pgaref'

import time
import redis
import logging
from redis.sentinel import Sentinel


class RedisHAClient():

    def __init__(self, host, port , monitor_group):
        self.host = host
        self.port = port
        self.group = monitor_group
        self.redis_master = None
        self.redis_slave = None
        self.redis_sentinel = self.bind_sentinel()
        self.redis_master = self.redis_sentinel.master_for(self.group, socket_timeout=0.1)
        self.redis_slave = self.redis_sentinel.slave_for(self.group, socket_timeout=0.1)

    def get_connection(self):
        return redis.StrictRedis(host=self.ip, port=self.port, db=0)

    def bind_sentinel(self):
        return Sentinel([(self.host, self.port)], socket_timeout=0.1)

    def discover_master(self):
        return self.redis_sentinel.discover_master(self.group)

    def discover_slaves(self):
        return self.redis_sentinel.discover_slaves(self.group)


if __name__ == '__main__':

    print 'Getting started'

    ha = RedisHAClient('127.0.0.1', 26379, 'mymaster')

    print 'Discovered masters: ', ha.discover_master()
    print 'Discovered slaves: ', ha.discover_slaves()

    print 'Writing value to master  => ', ha.redis_master.set('foo', 'panos')
    print 'Reading value from slabe => ', ha.redis_slave.get('foo')

    i  = 1
    while True:
        print 'Setting... ', i
        try:
            ha.discover_master()
            ha.redis_master.set('test', i)
            i += 1
        except redis.exceptions.ConnectionError:
            took = 1
            print 'Handling exception by discovering new master',
            print 'Time: ', took
            took +=1
            time.sleep(1)
        except redis.sentinel.MasterNotFoundError:
            pass

        print 'Going to sleep...'
        time.sleep(1)

