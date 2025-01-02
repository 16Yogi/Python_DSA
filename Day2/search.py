price = [298,305,320,301,292]

#price 298
def day1Price():
    for i in range(len(price)):
        if price[i] == 0:
            print(price[i])
            break
# day1Price()


userIn = int(input("check price:"))
def daySearch():
    for i in range(len(price)):
       if i == userIn-1:
        print(f"Day {userIn} Price is {price[i]}")         
daySearch()

# Sample price list
# price = [100, 200, 150, 300, 250]

# # User input for the day (1-based index)
# userIn = int(input("Enter the day number to check the price: "))
# def daySearch(userIn):
#     if 1 <= userIn <= len(price):
#         print(f"Day {userIn} Price is: {price[userIn - 1]}")
#     else:
#         print("Invalid day number. Please enter a number between 1 and", len(price))
# daySearch(userIn)

# day3 price  
# def day3Price():
#     for j in range(len(price)):
#         if 
# day3Price()