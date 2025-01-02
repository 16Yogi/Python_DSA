price = [298,305,320,301,292]


print(f"1. Choose 1 for insert\n 2. Choose 2 for Update\n 3. Choose 3 for Delete\n 4. show Result")
opr = int(input("Task input:"))

if opr == 1:
    insertVal = int(input("Insert value:"))
    indexVal = int(input("Enter index:"))
    def insertOpr():
        res = price.insert(indexVal,insertVal)
        if res == True:
            print("Data inserted")
        else:
            print("Data not inserted")
    insertOpr()
elif opr == 2:
    updateVal = int(input("Update value:"))
    indexVal = int(input("Enter index:"))
    def updateOpr():
        for i in range(len(price)):
            if i == indexVal:
                price[i] = updateVal
                break
    updateOpr()        
elif opr == 3:
    deleteVal = int(input("Delete value:"))
    indexVal = int(int("Enter Index:"))
    def deleteOpr():
        for i in range(len(price)):
            if i == indexVal:
                price.remove(indexVal)
                break
    deleteOpr()
elif opr == 4:
    def showResult():
        print(price)
    showResult()
else:
    print("Operation not found")