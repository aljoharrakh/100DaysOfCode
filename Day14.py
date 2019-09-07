menu=["milk","bread","juice","Vegetables","cheese","Fruits"]
price=[7,2,6,4,3,9]
cust=[]
copy=[]
bil=0.0
x=1
while True:
    for i in range(len(menu)):
        print (i,"-"+menu[i]+" , price is ",price[i])
    ch=input("write whar you want to buy from menu :(write finish to exit) ")
    if ch == "finish":
        break
    elif ch in menu:
      item = int(input("enter item number : "))
      cust.append(menu[item])
      copy.extend(cust)
      bil+=price[item]
      x+=1
    else:
        print("There is nothing written in menu , try agine")
if x==0:
   print("Thank you!")
else:
   print("your things in your bag are ", cust)
   print("your bil is ",bil,"\n Thank you!")



