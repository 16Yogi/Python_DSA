# numbers = [1, 23, 12, 43, 556, 745, 8, 65, 2, 5, 34, 12]
# duplicates = [] 
# for i in range(len(numbers)):
#     # print(i)
#     for j in range(i+1, len(numbers)):
#         # print("as",j)
#         # print(i)
#         if numbers[i] == numbers[j] and numbers[i] not in duplicates:
#             duplicates.append(numbers[i])
#             print(numbers[i], "is a duplicate")

# for num in duplicates:
#     print(f"Indexes of {num}: ", [i for i, x in enumerate(numbers) if x == num])

# -----------------------------


# this is not shorted way
# list1 = [1, 23, 12, 43, 556, 745, 8, 65, 2, 5, 34, 12]
# list2 = []
# result = []
# def dupicate():
#     for i in list1:
#         list2.append(i)
#     for j in list2:
#         if i == j:
#             result.append(j) 
#     print(result)        
# dupicate()


numbers = [1, 23, 12, 43, 556, 745, 8, 65, 2, 5, 34, 12]
dup = []
for i in range(len(numbers)):
    # print(i)
    for j in range(i+1,len(numbers)):
        if numbers[j] == numbers[i] and numbers[i] not in dup:
            dup.append(numbers[i]) 
            print(f"duplicate value:{numbers[i]}")

for ind in dup:
    print(f"index:{ind}",[i for i, x in enumerate(numbers) if x == ind ])

    # [i for i, x in enumerate(numbers) if x == num]