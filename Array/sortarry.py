arr = [12,341,3,5,1,3,90]
# def sort_arr(arr):
#     for i in range(0,len(arr)):
#         for j in range(i+i,len(arr)):
#             # print(arr[j])
#             if arr[i] < arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#                 # print(f"{arr[i],arr[j]}")
#         # print(f"fs: {arr[i]}")
#     print(arr)
# sort_arr(arr)

def sort_arr(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] >= arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    print(arr)
sort_arr(arr)