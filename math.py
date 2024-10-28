import math
a = math.sin(math.pi)
print(a)
print(math.sqrt(2984703875463.775865847385757938576))


import random
print(random.randint(1,20))

num=input(random.randint(1,1000000000))
num = int(num)

for i in range (2,num) :
    if num%i == 0 :
        print("number is not prime")
else :
     print ("number is prime")
