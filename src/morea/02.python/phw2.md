---
title: "Practice HW2"
published: true
morea_id: phw2
morea_type: experience
morea_sort_order: 5
morea_summary: "Binary & Python Variables"
morea_labels:

---
# Practice HW2: Binary, UNIX, & Python Variables

<!--{% include wod-times.html Rx="<10 min" Av="10-20 min" Sd="20-30 min" DNF="30+ min" %}-->

## Binary Encoding

1. How many pieces of information can be conveyed with a single bit?
1. How many bits would you need to represent each of the 50 United States using a unique permutation of bits?
1. How many bits are in a byte?
1. What is the binary representation of the number 3?
1. What is the encoding standard used to convert text into ordinal numbers?

## A simple python program

1. Create a folder `phw2_uLogin` where you replace `uLogin` with your Drew e-mail address before the @ sign.
2. Go into this folder by typing `cd phw2_uLogin` and create a python file: `touch hello_variable.py`
3. Edit the file (`ped hello_variable.py`):
    4. Create a variable to store your first name
    1. Print "Hello, my name is ..." and replace the ellipsis (...) with the variable that is storing your first name.
    1. Add a comment at the top of the file that explains what your program does.
4. Copy your python file `hello_variable.py` to `hello_me.py`.
4. Run your python program: `python3 hello_me.py`
5. Create a second program called `tips.py`, that:
    1. Has 4 variables:
        * meal: holds the value of the meal ($53.48)
        * tax: holds the tax percentage (7%)
        * tip: holds the tip percentage (18%)
        * total: holds the total of the meal. Proper tipping technique dictates that the tip should be calculated based on the total cost of the meal, before tax is applied.
    1. Prints the contents of the total variable with a leading dollar sign ($).
4. Run your python program: `python3 tips.py`. The total should be `$66.85`
5. Once you're satisfied that your programs are working correctly, zip it for submission:
    - `cd ..`
    - `zip phw2_uLogin.zip phw2_uLogin/*`

## Types & Arithmetic

Try to answer the following questions without typing them in to the `python3` interpreter, as you would on an exam or quiz.

1. Given the following values, what are their types:
    1. True
    1. 'True'
    1. 3 + 7j
    1. 34,756
    1. 98.7
    1. "98.7"
    1. "NY Giants"
2. If the following statements are executed in order, what will be the values of each variable?
    1. d = 7
    1. c = 3
    1. p = c / d
    1. q = d // c
    1. r = d % c
    1. z = 5 * r ** q
3. What would be an appropriate name and data type for the following variables:
    1. The name of the Super Bowl MVP
    1. The number of Vince Lombardi trophies a team has won
    1. The average number of touchdown passes per game



## UNIX Command Overview

For each of the following commands:

A. Briefly describe what it does in your own words. Example: 

    wget downloads files from the internet

If you don't know what a command does, google it. I recommend throwing the word "man" (short for manual) in front of the command.

B. Write a template of how the command is used -- indicate arguments in [brackets]. For example, a template for the wget command would look like this:

    wget [url to download]

Alternatively, the zip command to submit an assignment might look like this:

    zip [folder].zip [folder]/*

C. Take a screenshot of using the command on your terminal, cropping out irrelevant parts. You should make sure the command works in the screen shot.

   Example for **wget**:

   <a href="wget.png"><img src="wget.png" width="500"/></a>

   The example for **remove** also needs to show the file is no longer there:

   <a href="rm.png"><img src="rm.png" width="300"/></a>

Your document should be organized by command -- for example, you should describe the ls command, give its template, and include a cropped screenshot before moving on to the next command, pwd.

**Commands:**

1. ls
1. pwd
1. cd
1. touch
1. mkdir
1. cp
1. mv
1. rm
1. ped
1. cat
1. zip    
1.  .      (not a command, use in conjunction with another command)
1. ..      (not a command, use in conjunction with another command)
1. tab     (no screenshot necessary)
1.  ↑      (no screenshot necessary)

**How to take *& crop* a Screenshot**

- Windows: [www.ehow.com/how_6801557_crop-screen-shot.html](www.ehow.com/how_6801557_crop-screen-shot.html)
- Mac: [http://www.ehow.com/how_4559274_take-edit-screen-shots-mac.html](http://www.ehow.com/how_4559274_take-edit-screen-shots-mac.html)
    - Make sure to use Command (⌘)-K rather than control-K as the article states.



<!-- Allow 45 minutes for all? -->

<!--## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="NGK61X9ry9c" %}

{% include wod-warning.html %}

### Solutions to Questions

<a href="types.png"><img src="types.png" width="200"/></a>-->