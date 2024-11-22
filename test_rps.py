#Malcolm Nov 20

import random

player1 = random.choice(['rock','paper','scissors'])
player2 = random.choice(['rock','paper','scissors'])
def test_rps(player1,player2):
#a string that will be one of rock paper scissors
    # function will return player 1 if player 1 wins
    if (player1[0] and player2[2]) or (player1[3] and player2[1]) or (player1[3] and player2[2]):
        return player1
    #function will return player 2 if player 2 wins
    elif (player2[0] and player1[2]) or (player2[3] and player1[1]) or (player2[3] and player1[2]):
        return player2
    # if tie return tie 
    else :
        return tie
print (test_rps())
