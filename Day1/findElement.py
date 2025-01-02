list1 = [1,23,1,321,42,43,12,6,875,90]  #search -12

for i in list1:
    if i == 23:
        print(f"Element:{i}")
        break


def findElement(num1):
    for i in range(len(list1)):
        if list1[i] == num1:
            print(f"Element:{list1[i]}")
            break
findElement(23)