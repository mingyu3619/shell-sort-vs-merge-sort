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


#arr=[14,1,3,4,12,113,12,1,32,414,23,5]
#print("arr:",arr,"\n","merged:",merge_sort1(arr))


#print(arr[0])
