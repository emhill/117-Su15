# Simulate Pick 4 lottery game - selecting ping pong balls at random
# Modified to figure out if the user entered the winning number

from random import *
import sys

# define constants that are easy to change so that our
# program is flexible
NUM_PICKS = 4
MIN_VALUE = 0
MAX_VALUE = 9

NUMFORMAT="####"

pickedNum = input("What is your pick? (Format: " + NUMFORMAT + ") ")

######  handle bad input ######

# Check that user enters a string that contains only numbers
if not pickedNum.isdigit():
    print("Your number must contain only numbers")
    sys.exit()

# If we get to here, we know the user's input is all digits

# User enters a number that is not four digits long
if len(pickedNum) != 4:
    print("Your number must contain four numbers")
    sys.exit()

# Generate the random number
winningNum = "" # start it as empty

for i in range(NUM_PICKS):
    # generate a random number
    # add the random number to the previous random number
    winningNum += str(randint(MIN_VALUE,MAX_VALUE))

print("The winning Pick 4 lottery number is ", winningNum)
print()

if winningNum == pickedNum:
    print("Congratulations!  You are very lucky and rich!")
    print("We should be friends!")
else:
    print("Sorry, you lost.")
