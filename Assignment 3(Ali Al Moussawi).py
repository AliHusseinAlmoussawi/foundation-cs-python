Products=[['Milk',10],['Bread',4],['Water',3],['Beverage',5],['Candy',3],['Yogurt',7],['Rice',6],['Mayo',9]]
Order=list()
def Add_Item(Order,Products):
        item = input("Add an item:")
        quant = int(input("Enter the quantity:"))
        for i in range(len(Products)):
            if item == Products[i][0]:
                Order.append([item,Products[i][1],quant])
                break
        else:
            print("No item found")
        return Order
def Total_Bill(Order):
    total = 0
    for i in range(len(Order)):
        total += (Order[i][1] * Order[i][2])
    return total

def Bill_With_Coupon(total,coupon):
    total = total - coupon
    return total

while True:

    print("Welcome to Aamo El Dekanje POS system:")
    print("1: Start a new order")
    print("2: Close the program")
    n = int(input("Enter your choice (1 or 2):"))

    if n == 2:
        print("Bye Bye")
        break

    if n == 1:
        print("What do you like to do?")
        while n != 2:
            print("1: Add a new item")
            print("2: Check the total of the bill")
            print("3: Add a coupon")
            print("4: Checkout")
            m = int(input("Choose one of the upper operations:")) #Choice among the upper operations

            if m == 1:
                Order = Add_Item(Order, Products)
                print("What do you like to do again?")
                continue
            if m == 2:
                total = Total_Bill(Order)
                print("Your total bill is: ", total)
                print("What do you like to do again?")
                continue
            if m == 3:
                total = Total_Bill(Order)
                Coupon = int(input("Enter the coupon value:"))
                Final_bill = Bill_With_Coupon(total, Coupon)
                print("What do you like to do again?")
                continue
            if m == 4:
                total = Total_Bill(Order)
                Coupon = int(input("Enter the coupon value:"))
                Final_bill = Bill_With_Coupon(total, Coupon)
                for i in range(len(Order)):
                    print("Item: ", Order[i][0], " Quantity: ", Order[i][2])

                print("Total bill without coupons: ", total)
                print("Total bill with coupons is: ", Final_bill)
                n=2





