"""
thread basics: start 5 copies of a function running in parallel;
uses time.sleep so that the main thread doesn't die too early--
this kills all other threads on some platforms; stdout is shared:
thread outputs may be intermixed in this version arbitrarily.
"""

import _thread as thread, time

def counter(myId, count):                        # function run in threads
    for i in range(count):
        time.sleep(1)                            # simulate real work
        print('[%s] => %s' % (myId, i))         # myid= any number

for i in range(5):                               # spawn 5 threads, which mean 5 round
    thread.start_new_thread(counter, (i, 5))     # each thread loops 5 times #i=my id , count= 5, where 5=0to4 in a single thread

time.sleep(6)
print('Main thread exiting.')                    # don't exit too early
