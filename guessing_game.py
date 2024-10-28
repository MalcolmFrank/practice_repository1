#Malcolm 28 Oct 2024
#guessinng_game.py
#a guessing game where the computer gives hints after guess

import random
    # randomly generate a number
num = random.randint(1,100)
    #make a loop
    #track of guesses
attempts = 0
guess = 0
    #loop should continue until user guesses correct or runs out if attempts
while (guess != num) and (attempts <= 4):
    #ask user for a number
    guess = int(input("enter a random number between 1,100 you have 5 attepts to guess: "))
    attempts += 1
        #if correct say they won
    if guess == num :
        print("winner")
        #if to low say to low
        #using elif and else for other values makes the code run faster
    elif guess < num :
        print("to low")
        #if to high say to high
    else :
        print("to hight")
        #after user guesses correctlly tell them how many attempts it took them
if attempts == 5 :
    print ("you lost")
else :
    print(f"you guessed it in {attempts} attempts")
