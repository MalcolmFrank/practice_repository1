#Malcolm 14 Nov
#practice_14_nov
#making a programm that checks numbers to see if it's between 10-20 and if it's a "not" string

##functions
def in1020(a,b):
        #check if a is between 10 and 20 if so say true
    if (a >= 10) and ( a <= 20):
        return True
        #check if b is between 10 and 20 if so say true
    elif (b >=10)and (b <= 20):
        return True
        #if both a and b are not between 10 and 20 return false
    return False

def not_string(string):
        #check if "not" starts the string and return as if

        #otherwise return "not" + string
    pass
alien = {"home_planet":"Mars",
         "number of ears":0,
         "number of eyes":7,
         "skin color": "orange"}

##code
print(alien.keys())
print(alien.values())
print(alien.items())
a = int(input("enter a number: "))
b = int(input("enter a second number: "))
print(in1020(a,b))


