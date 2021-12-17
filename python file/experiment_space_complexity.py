from merge_sort2 import mergesort2_call
from merge_sort import merge_sort1
from shell_sort import shell_sort

import numpy as np

import matplotlib.pyplot as plt
import psutil
import os

def space_check():
    pid = os.getpid()
    current_process = psutil.Process(pid)
    return current_process.memory_info()[0] / 2. ** 20


merge1_memory=[]
merge2_memory=[]
shell_memory=[]
#n=100000
n=range(0,6000,1000)
for i in n:

    arr_before=np.random.rand(i)
    print(i,arr_before.shape)
    start_merge1=space_check()
    ##
    pid = os.getpid()
    print(pid)
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    merge_sort1(arr_before.copy())
    ##
    pid = os.getpid()
    print(pid)
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    ##
    end_merge1=space_check()
    merge1_memory.append(end_merge1-start_merge1)

    start_merge2=space_check()
    pid = os.getpid()
    print(pid)
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    mergesort2_call(arr_before.copy())
    ##
    pid = os.getpid()
    print(pid)
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    ##
    end_merge2=space_check()
    merge2_memory.append(end_merge2 - start_merge2)

    start_shell=space_check()
    ##
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    ##
    shell_sort(arr_before.copy())
    ##
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    ##
    end_shell=space_check()
    shell_memory.append(end_shell - start_shell)
########################## space
print(merge1_memory)
print(merge2_memory)
print(shell_memory)

plt.plot(n,merge1_memory,label="merge1",ms=1)
plt.plot(n,merge2_memory,label="merge2",ms=1)
plt.plot(n,shell_memory,label='shell',ms=1)

plt.xlabel("Number of list element")
plt.ylabel("kb")
plt.legend()
plt.show()