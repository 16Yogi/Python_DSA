arr = [12, 35, 1, 10, 34, 1]
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
    # arr = [12, 35, 1, 10, 34, 1]
    # arr = [10, 5, 10]
    arr = [10, 10, 10]
    print(secondLarget(arr))