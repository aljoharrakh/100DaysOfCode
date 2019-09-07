ch=1
while ch==1:
    print("Enter three of the skills you are good at")
    list=[",","",""]
    for i in range (len(list)):
       list[i]=input("1- ")
    skills=tuple((list[0],list[1],list[2]))
    print("your skills are :")
    for i in skills:
       print (i)
    print(", and first skill is ",skills[0:1])
    ch=int(input(" if you want rewrite your skills prass 1, no prass 0"))
    if ch==1:
      del skills
print ("Thank you !")


