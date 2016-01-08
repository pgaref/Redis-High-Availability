# Redis-High-Availability
Playing around with Redis High Availability


#Starting Redis

You can start redis server just by typing: 
 * redis-server

We are going to run all instances locally so we are using custom configuration:
 * redis-server conf/servers/redis1.conf &
 * redis-server conf/servers/redis2.conf &


#Starting Sentinels
 * redis-sentinel conf/sentinels/sent1.conf &
 * redis-cli -p 26379

127.0.0.1:26379> sentinel master mymaster
 1) "name"
 2) "mymaster"
 3) "ip"
 4) "127.0.0.1"
 5) "port"
 6) "6379"
 7) "runid"
 8) "a27614b640d37781ecb4f108ffe09e7e7080ec35"
 9) "flags"
10) "master"
11) "pending-commands"
12) "0"
13) "last-ping-sent"
14) "0"
15) "last-ok-ping-reply"
16) "400"
17) "last-ping-reply"
18) "400"
19) "down-after-milliseconds"
20) "1000"
21) "info-refresh"
22) "2274"
23) "role-reported"
24) "master"
25) "role-reported-time"
26) "152907"
27) "config-epoch"
28) "0"
29) "num-slaves"
30) "1"
31) "num-other-sentinels"
32) "0"
33) "quorum"
34) "1"
35) "failover-timeout"
36) "30000"
37) "parallel-syncs"
38) "1"

#Using redis-cli
 * redis-cli -p 6379
127.0.0.1:6379> get mykey
"A"
127.0.0.1:6379> set mykey B
OK

#Writing code to take advantage of Redis HA



