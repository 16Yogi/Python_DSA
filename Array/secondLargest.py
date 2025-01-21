# arr = [12, 35, 1, 10, 34, 1]
# arr = [10, 5, 10]
# arr = [10, 10, 10]
def secondLarget(arr):
    n = len(arr)
    arr.sort()
    
    for i in range(n-2,-1,-1):
        # print(arr[i],end=" ")
        if arr[i] != arr[n-1]:
            return arr[i]
    return -1
# sort_arr(arr)  
if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    # arr = [10, 5, 10]
    # arr = [10, 10, 10]
    print(secondLarget(arr))


#------------------------------------------ 

# def secondLarg(arr):
#     arr_len = len(arr)
#     arr.sort()
#     for i in range(arr_len-2,-1,-1):
#         if arr[i] != (arr_len-1):
#             return arr[i]
#     return -1
# if __name__ == "__main__":
#     arr = [12, 35, 1, 10, 34, 1]
#     print(secondLarg(arr))


# arr = [12, 35, 1, 10, 34, 1]
# def secondLarg(arr):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]<arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i] 
#     # return arr #sort 
    
#     # get larget value
#     n = arr[0]
#     # print(n)
#     for i in range(len(arr)):
#         if arr[i]<n:
#             n=arr[i]

    # print(f"second largest:{arr[1]}")
    
    # k = arr[0]
    # return k
    # return arr
    # get second larget value
    # for i in range(len(arr)):
        # print(arr[i],end=" ") 
        
    # print(k)


# if __name__ == "__main__":
#     arr = [12, 35, 1, 10, 34, 1]
#     print(secondLarg(arr))
