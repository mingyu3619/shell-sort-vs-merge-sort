import random
import psutil
import os
import numpy as np
import matplotlib.pyplot as plt

#############################################################
def random_list(size):
    result=[]
    for v in range(size):
        result.append(random.randint(0,10000))
    return result
#############################################################
def mergesort2_call(arr):
    left=0;right=len(arr)-1
    return arr,left,right

def mergesort2(arr,left,right):
    if(right-left>=1):
        mid=(right+left)//2
        mergesort2(arr,left,mid)
        mergesort2(arr,mid+1,right)
        return merge_def(arr,left,mid,right)
    else:
        return

def merge_def(arr,left,mid,right):
    sum_arr = []
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
