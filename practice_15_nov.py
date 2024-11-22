#Malcolm nov 15

#make a function called uniqe square 
def unique_square(nums):
    #it should return the square of the number in the list
    squared = []
    for num in nums:
    #no repeats
        if num*num not in squared:
            squared.append(num*num)
    return squared
    
#code
print(unique_square([9,7,8,4,2]))
print(unique_square([8,7,6,8,9,3]))

import random

days=[i for i in range(1,366)]
for i in range(30):
    student_bday.append(re
