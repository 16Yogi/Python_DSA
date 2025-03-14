# def thirdLarg(arr):
#     len_arr = len(arr)
#     arr.sort()
#     for i in range(len_arr-3,-1,-1):
#         if arr[i] != (len_arr-1):
#             return arr[i]
#     return -1

# if __name__ == "__main__":
#     arr = [12, 35, 1, 10, 34, 1]
#     print(thirdLarg(arr))


# Python 3 program to find 
# third Largest element in 
# an array of distinct elements 


import sys 
def thirdLargest(arr, arr_size): 

	# There should be 
	# atleast three elements 
	if (arr_size < 3): 
		print(" Invalid Input ") 
		return
	

	# Find first 
	# largest element 
	first = arr[0] 
	for i in range(1, arr_size): 
		if (arr[i] > first): 
			first = arr[i] 

	# Find second 
	# largest element 
	second = -sys.maxsize 
	for i in range(0, arr_size): 
		if (arr[i] > second and
			arr[i] < first): 
			second = arr[i] 

	# Find third 
	# largest element 
	third = -sys.maxsize 
	for i in range(0, arr_size): 
		if (arr[i] > third and
			arr[i] < second): 
			third = arr[i] 

	print("The Third Largest", 
		"element is", third) 

# Driver Code 
arr = [12, 13, 1, 
	10, 34, 16] 
n = len(arr) 
thirdLargest(arr, n) 

# This code is contributed 
# by Smitha 
