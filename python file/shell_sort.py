def shell_sort(arr):
    size=len(arr)
    gap=size//2
    while gap > 0 :
        for i in range(0,gap):
            selection_sort(arr,i,size,gap)
        gap= gap//2
    return arr

def selection_sort(arr,first,size,gap):
    for i in range(first+gap,size):
        key=arr[i]
        j=i-gap
        while j>=first and arr[j] > key:
            arr[j+gap] = arr[j]
            j=j-gap
        arr[j+gap]=key

    return arr
#################################################

# arr1=[8,6,4,2,1,45,42]
# print(arr1)
# print(shell_sort(arr1))
