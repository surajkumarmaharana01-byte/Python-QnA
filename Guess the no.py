#1st MINI PROJECT
#GUESS THE NUMBER

import random

target=random.randint(1,100)

while True:
    userChoice=(input("Guess the Target or Quit(Q): "))
    if(userChoice=="Q"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success : Correct guess Bro!!")
        break
    elif(userChoice<target):
        print("Your Number was too small. Take a Bigger Guess.....")
    else:
        print("Your Number was too Big. Take a Smaller Guess......")


print("_____GAME OVER_____")