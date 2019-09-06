copy=[]
ch=1
while ch>0 :
     number = input("Enter float number :")
     list=[]
     if ((number.rfind('.'))>0):
        list.append(float(number))
        ch= int(input ("enter 0 to exit and 1 to contunus "))
     else:
         print ("you enter invalid number , try agine")
     copy.extend(list)

print (copy)