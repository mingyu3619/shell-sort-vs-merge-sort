import random
import psutil
import os
import numpy as np
import matplotlib.pyplot as plt
from shell_sort import shell_sort
#############################################################
def random_list(size):
    result=[]
    for v in range(size):
        result.append(random.randint(0,1000000))
    return result
###############################################################
def selection_sort(arr,first,last,gap):

    for i in range(first+gap,last):
        key=arr[i]
        j=i-gap
        while j>=first and arr[j] > key:
            arr[j+gap] = arr[j]
            j=j-gap
        arr[j+gap]=key

def shell_sort(arr):
    n=len(arr)
    gap=n//2
    while gap > 0 :
        for i in range(0,gap):
            selection_sort(arr,i,n,gap)
        gap= gap//2
    return arr

#############################################################
def mergesort2_call(arr):
    left=0;right=len(arr)-1
    return mergesort2(arr,left,right)

def mergesort2(arr,left,right):
    if(right-left>=1):
        mid=(right+left)//2
        mergesort2(arr,left,mid)
        mergesort2(arr,mid+1,right)
        return merge_def(arr,left,mid,right)
    else:
        return

def merge_def(arr,left,mid,right):
    sum_arr = []    ##merge 부분시작
    i = left
    j = mid+1
    while (i <= mid and j <= right):
        if (arr[i] < arr[j]):
            sum_arr.append(arr[i])
            i+=1
        else:
            sum_arr.append(arr[j])
            j+=1
    if (i>mid):
        sum_arr.extend(arr[j:right+1])
    if (j>right):
        sum_arr.extend(arr[i:mid+1])
    arr[left:right+1] = sum_arr
    return arr
#############################################################
def merge_sort1(arr):
    half=len(arr)//2
    if half==0:
        return arr
    arr_left=arr[:half]
    arr_right=arr[half:]

    left_result=merge_sort1(arr_left)
    right_result=merge_sort1(arr_right)
    return merge(left_result,right_result)

def merge(left_arr,right_arr):
    i=0;j=0
    sum_arr=[]

    while(i<len(left_arr) and j<len(right_arr)):
        if (left_arr[i] > right_arr[j]):
            sum_arr.append(right_arr[j])
            j+=1
        else:
            sum_arr.append(left_arr[i])
            i+=1
    if (i==len(left_arr)):
        sum_arr.extend(right_arr[j:])
    if(j==len(right_arr)):
        sum_arr.extend(left_arr[i:])
    return sum_arr
#############################################################
m1=[]
m2=[]
s=[]
merge1_memory=[]
merge2_memory=[]
shell_memory=[]
        #[5000           10000          15000            20000              25000
#memory=[0.125   0.453125               0.6796875        0.70703125         0.9375

print('-'*20,"merge1")
n=range(0,10000,2000)
for i in n:
##merge1
    before_sort=random_list(i)
    print("i:",i,"size:",before_sort.__sizeof__())
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB_s = current_process.memory_info()[0] / 2.**20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB_s: 9.3f} KB")
    merge_sort1(before_sort)
    pid2 = os.getpid()
    current_process2 = psutil.Process(pid2)
    current_process_memory_usage_as_KB_e = current_process2.memory_info()[0] / 2.**20
    print(f"AFTER CODE: Current memory KB   : {current_process_memory_usage_as_KB_e: 9.3f} KB")
    used_memory=current_process_memory_usage_as_KB_e-current_process_memory_usage_as_KB_s
    print(used_memory)
    merge1_memory.append(used_memory)
##merge2

    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB_s = current_process.memory_info()[0] / 2. ** 20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB_s: 9.3f} KB")
    mergesort2_call(before_sort)
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB_e = current_process.memory_info()[0] / 2. ** 20
    print(f"AFTER CODE: Current memory KB   : {current_process_memory_usage_as_KB_e: 9.3f} KB")
    used_memory = current_process_memory_usage_as_KB_e - current_process_memory_usage_as_KB_s
    print(used_memory)
    merge2_memory.append(used_memory)
###shell
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB_s = current_process.memory_info()[0] / 2. ** 20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB_s: 9.3f} KB")
    shell_sort(before_sort)
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB_e = current_process.memory_info()[0] / 2. ** 20
    print(f"AFTER CODE: Current memory KB   : {current_process_memory_usage_as_KB_e: 9.3f} KB")
    used_memory = current_process_memory_usage_as_KB_e - current_process_memory_usage_as_KB_s
    print(used_memory)
    shell_memory.append(used_memory)


        #[5000         10000        15000    20000   25000       30000      35000
#memory=[0.0078125  0.20703125  0.1171875  0.09375  0.1796875  0.41796875   0.45703125]


print('-'*20,"shell")
#
#n=range(0,50000,5000)

#[5000         10000         15000      20000
#[0.00390625      0.0       0.02734375  0.03125
#before_sort=np.random.randint(10000,size=i)
#print(before_sort)


print(merge1_memory)
print(merge2_memory)
print(shell_memory)
#
# plt.plot(n,merge1_memory,label="merge1",ms=1)
# #plt.plot(n,merge2_memory,label="merge2",ms=1)
plt.plot(n,merge1_memory,label="merge1",ms=1)
plt.plot(n,merge2_memory,label="merge2",ms=1)
plt.plot(n,shell_memory,label="shell",ms=1)
plt.xlabel("Number of list element")
plt.ylabel("Memory(kb)")
plt.legend()
plt.show()
