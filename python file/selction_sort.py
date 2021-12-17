def selection_sort1(arr):
    i=j=key =0
    length=len(arr)

    for i in range(1,length):
        key=arr[i] ## key 값 선택
        j=i-1      ## key 왼쪽과  비교
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j=j-1
            print(id(i),id(j),id(key))
        arr[j+1]=key

    return arr


##########################################

# arr2=[4,1,6,2,5,1,2,5]
#
# print(arr2)
# print(selection_sort1(arr2))

