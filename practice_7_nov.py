#Malcolm 7 Nov
#practice_7_nov.py
#the goal is to find if a number is within 10 

##function

#write a function called check_within_ten that takes a number as a parameter and returns the value true if the the nuber is within 10 of 100 and false if otherwise
def check_within_ten(num):
    #i need to compare num to 100
    #subtract 100 from 10 and if it's between 10 0 or -10 then it's within ten
    #return the function if not it will appear none
    if num - 100 in range (-10,10) :
        return True
    #if it's not within ten say number is not within ten
    else :
        return False
    #return the function if not it will appear none
    
#test the followinf by running the following code
print(check_within_ten(73))
print(check_within_ten(95))
print(check_within_ten(103))
print(check_within_ten(117))
    
