Sent="Please, I want {} sandwishes and {} donutes "
#first
Sent=Sent.replace("I","we")

#second
Sent=Sent.format(5,7)
#last
Sent=Sent.replace("a","A",len(Sent))
print(Sent)