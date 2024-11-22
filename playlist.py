#Malcolm 8 Nov
#playlist.py
#i'm making a playlist that you are able to chose a song and skip

import random

def button1():
    song.append(song[0])
    song.pop(0)
def button2():
    song.insert(0, song.pop(-1))

def button3():
    pass

def button4():
    pass

def button5():
    pass

#make a playlist that has at least 5 songs
song = ['a','b','c','d','e']

#ask a user to input a choice between 1 & 5 (explain what each button does)

print('''enter a number between 1 and 5
1 will move ...
2 will
3 will
4 will
5 will
you can keep entering number 1 - 4
5 will play the playlist''')

button = ''

while button != '5':
#make a choice to skip song aka last song to beginning
    if button == '1':
        button1()
#make a choice to swaps first two songs
    elif button == '2':
        button2()
#make a choice to shuffle playlist
    elif button == '3':
        button3()
    elif button == '4':
        button4()
    elif button == '5':
        continue
button5()

