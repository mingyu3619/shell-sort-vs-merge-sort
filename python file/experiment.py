from merge_sort2 import mergesort2_call,mergesort2
from merge_sort import merge_sort1
from shell_sort import shell_sort
import time
import numpy as np
import random
import matplotlib.pyplot as plt
import psutil
import os

merge1_time=[]
merge2_time=[]
shell_time=[]

#n=100000
n=range(0,17000,1700)
for i in n:
    print(i)
    before_sort=np.random.randint(10000,size=i)

    start_s = time.time()
    shell_sort(before_sort.copy())
    shell_time.append(time.time() - start_s)


    start_m1=time.time()                ##mergesort1
    merge_sort1(before_sort.copy())
    merge1_time.append(time.time()-start_m1)


                   ##mergesort2
    merge2_arg=mergesort2_call(before_sort.copy())
    start_m2 = time.time()
    mergesort2(merge2_arg[0],merge2_arg[1],merge2_arg[2])
    merge2_time.append(time.time()-start_m2)




######################### time
print(merge1_time)
print(merge2_time)
print(shell_time)

plt.plot(n,merge1_time,label="merge1",ms=1)
plt.plot(n,merge2_time,label='merge2',ms=1)
plt.plot(n,shell_time,label='shellsort',ms=1)

plt.xlabel("Number of list element")
plt.ylabel("time(seconds)")
plt.legend()
plt.show()

######################### time

