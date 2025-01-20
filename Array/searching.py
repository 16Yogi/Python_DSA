arr = [10,20,30,40,50,60]
n = len(arr)
key = 30
def search_element(arr,n,key):
    for i in range(n):
        if arr[i] == key:
            print(f'element:{arr[i]}')
            # break
        # else:
            # print("Not found")
    return -1
search_element(arr,n,key)