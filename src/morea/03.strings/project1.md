---
title: "Project 1"
published: true
morea_id: project1
morea_type: experience
morea_sort_order: 5
morea_summary: "Using Strings & Functions"
morea_labels:

---
# Project 1: Using Strings & Functions
<!--
{% include wod-times.html Rx="<10 min" Av="10-20 min" Sd="20-30 min" DNF="30+ min" %}-->

## Setup

  * `mkdir project1_uLogin1_uLogin2`
  * `cd project1_uLogin1_uLogin2`
  * `touch bye.py convert.py fun.py string.py`

***Don't forget to add a comment at the top of each program with your & your partner(s) names and what the program does.***

## bye.py

3. Edit the file (`ped bye.py`):
    4. Create a variable that stores a name    
    1. Print "Goodbye, ...!" and replace the ellipsis (...) with the variable that is storing your last name.
    1. Add a comment at the top of the file that explains what your program does and who the authors are.
4. Run your python program: `python3 bye.py`
4. Copy your python file `bye.py` to `byebye.py`.

## convert.py

Create a program `convert.py`, that takes a measurement in inches as input and outputs the equivalent length in centimeters. Your program should have 2 variables:

  * `inches`: holds the length in inches (input from the user)
  * `cm`: holds the length in centimeters. To convert inches to cm, multiply by 2.54.

Your program shold print the values of both variables with a string description, such as: `"I inches = C cm"`, replacing I & C with the values of your variables.

For example:

| **inches** | **cm** | **output** |
|:---:|:---:|:---:|
| 1 | 2.54 | 1 inches = 2.54 cm |
| 12 | 30.48 | 12 inches = 30.48 cm |
| 39.5 | 100.33 | 39.5 inches = 100.33 cm |


## fun.py

Write a program `fun.py` that takes a float as input from the user and prints out the following information using the math module:

  1. The ceiling of the number (e.g., `ceiling(3.75)` is 4)
  1. The number rounded to 0 decimal places
  1. The factorial of the rounded number


## string.py

Write a program `string.py` that takes a string as input from the user and prints the string after performing the following two mangle operations:

  1. Swaps upper and lower case letters
  1. Removes the third and third to last characters
  
Finally, print only the middle 3 letters using the substring or splice operation (`[:]`).
  
For example:

| **string** | **Mangled Output** | **Middle 3** |
|:---:|:---:|:---:|
| Monty Python | mOTY pYTON | 'y P' |
| hello! | HEO! | 'ell' or 'llo' |
| oh | OH | '' |

## Submission

Once you're satisfied that your programs are working correctly, zip it for submission:

  - `cd ..`
  - `zip project1_uLogin1_uLogin2.zip project1_uLogin1_uLogin2/*`

Upload your zip file to Google Classroom.