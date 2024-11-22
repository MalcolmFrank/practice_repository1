#Malcolm 13 Nov
#practice_13_nov
#make a programm that finds which value is greater 

a=int(input("enter a number: "))
b=int(input("enter a second number: "))
if a < b :
    print(b)
else :
    print (a)

##function
#create a function called find_max(a,b) that returns the large of a & b
def find_max(a,b):
    if a < b :
        return (a)
    return (b)
    
def two_two(a,b,c,d,e,f):
    stuff = [a,b,c,d,e,f]
    stuff.sort()
    return stuff[-1], stuff[-2]
