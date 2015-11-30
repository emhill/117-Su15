---
title: "Project 5"
published: true
morea_id: project5
morea_type: experience
morea_sort_order: 14
morea_summary: "ConnectFour"
morea_labels:

---

# Project 5: ConnectFourIn this project you will develop a ConnectFour game using object-oriented concepts. **You may work as a team of 2-3 or alone.**Begin by downloading [project5.zip](project5.zip) and unzip it. You should see the following files:

   * `game.py`: main program to play game **DO NOT MODIFY**
   * `connectfour.py`: where you will write your project code
   * `csplot.py`: helper functions to draw the game **DO NOT MODIFY**You should only have to modify `connectfour.py` and ***not*** `csplot.py` or `game.py`.
## Step 1: Understand `ConnectFour`

Open up `connectfour.py` and look at the `ConnectFour` class. Familiarize yourself with its attributes (fields) and how the methods are implemented. Pay special attention to how you might implement making a move and determining who the winner is.

Run `game.py` & submit a screenshot for check point 1. You may have to hit Control-C to kill the game if closing the window does not work.

## Step 2: `makeMove`

Implement the `makeMove` method. Adhere to the method's comment description when implementing the method.

Then, test `makeMove` by running `game.py`. Take a screenshot & submit a screenshot for check point 2 (make sure to show your code & a board with colored tiles).

## Step 3: `_isWon`

Implement `_isWon` to determine if a player has won. You may want to try implementing it for the tic tac toe game we looked at in class (`tictactoe2.py`), and then see how your solution could be adapted to go from looking at 3 spots to 4.

Run `game.py` to test your game. When you've tested that both players can win, you're ready to submit.

<!--Draw a UML diagram of the given code. Example for the Date class:
-->

## Extra Credit: Smarter computer player

For extra credit, change `_computerMakeMove` to be more intelligent & actively prevent the human player from winning.

## Extra Credit: Checkers

Implement support in `ConnectFour` to play a checkers game. Write your own `checkers.py` main program to run that instead of `ConnectFour`.

## Submission

Make sure you've added your name to the comments at the top of the file, that your program contains comments and follows good programming style.

Once you’re satisfied that your game is working correctly, zip it for submission:

  * `cd ..`
  * `zip project5_uLogin.zip project5_uLogin/*`
<!--*Assignment adapted from [Harvey Mudd's CS 5 Fun with Images](https://www.cs.hmc.edu/twiki/bin/view/CS5/FunWithImagesGold2010).*-->