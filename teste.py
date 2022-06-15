#!/usr/bin/python3

import psutil
var=psutil.cpu_times()
#scputimes(user=32597.3, nice=222.66, system=11311.57, idle=150881.0, iowait=172.65, irq=0.0, softirq=519.62, steal=0.0, guest=0.0, guest_nice=0.0)

#print(var.user)

print(psutil.cpu_count())
print(psutil.cpu_stats())
print(psutil.cpu_freq())
print(psutil.getloadavg())
print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_usage("/"))
print(psutil.disk_io_counters(perdisk=True))
print(psutil.net_io_counters(pernic=True))
print(psutil.net_connections(kind="inet4"))
print(psutil.net_if_stats())

p = psutil.Process()
with p.oneshot():
     p.name()  # execute internal routine once collecting multiple info
     p.cpu_times()  # return cached value
     p.cpu_percent()  # return cached value
     p.create_time()  # return cached value
     p.ppid()  # return cached value
     p.status()  #

print(p)
