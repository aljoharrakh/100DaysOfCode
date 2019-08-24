x="apple"
y="orange"
z="limon"
basket=x+y+z
print("Basket befor spliting is ",basket)
print("******************************")
print("First solution to display the Basket after spliting is ",basket.split("e"))
print("******************************")
total=len(basket)
basket="["
for i in range(total+1):
    if (i==len(x)):
        basket+=x+","
        i+1
    elif(i==len(y)+len(x)):
           basket += y + ","
           i+1
    elif(i == total):
           basket += z + "]"
           break
    else:
         i+1
print("Second solution to display the Basket after spliting is ",basket)
