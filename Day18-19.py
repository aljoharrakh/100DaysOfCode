print("*********welcome to Supermarket**********")
menu = ["milk", "bread", "juice", "Vegetables", "cheese", "Fruits"]
price = [7, 2, 6, 4, 3, 9]
bill = 0
cust = []
finalyOrder=[]
while True:
    ch=int(input("1-Go to shopping\n2-Go for the bag\n3-Delete all contents of the bag\n4-delete specific purpose \n5-Going to pay the account\n6-exit\nenter number of choice:"))
    if ch==1:
        while True:
            for i in range(len(menu)):
                print (i, "-" + menu[i] + " , price is ", price[i])
            item = int(input("enter item number for what you want to buy from menu :(write -1 to exit) "))
            if item == -1:
                break
            else:
                cust.append(menu[item])
                bill += price[item]
    elif ch==2:
        print("******Bag******")
        if len(cust)==0:
           print("there is no thing!")
        else:
            print (cust)
    elif ch==3:
        option=input("are you sure ?")
        if option=="yes"or option=="yes":

            cust.clear()
            bill=0
    elif ch==4:
        if len(cust) == 0:
            print("there is no thing to delete!")
        else:
            print (cust)
            delete=input(" write item name to delete ")
            cust.remove(delete)
            for i in range (len(menu)):
                if menu[i]==delete:
                    bill-=price[i]
    elif ch==5:
        print ("********Bill*********")
        finalyOrder.extend(cust)
        for i in range (len(finalyOrder)):
            print (i,"-",finalyOrder[i],"count: ",finalyOrder.count(finalyOrder[i]))
        print ("your bill is ",bill)
        finalyOrder.clear()
        cust.clear()
        bill = 0
    else:
        break
print ("thank you for visiting !")

