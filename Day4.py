import random
IntNum=10
FloNum=5.5
CompNum=1+2j
print(IntNum,' number is ',type(IntNum))
print(FloNum,' number is ',type(FloNum))
print(CompNum,' number is ',type(CompNum))
print('***********************************')
print('convert',IntNum,' to float is ',float(IntNum))
print('convert',FloNum,' to integer is ',int(FloNum))
print('convert',IntNum,' to complex is ',complex(IntNum))
print('convert',FloNum,' to complex is ',complex(FloNum))
print('***********************************')
print('Your lucky number is ',random.randrange(1,10))