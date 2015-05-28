---
title: "HW4"
published: true
morea_id: hw4
morea_type: experience
morea_sort_order: 5
morea_summary: "Using Strings & Functions"
morea_labels:
 - due 6/3
---
# HW4: Using Strings & Functions
<!--
{% include wod-times.html Rx="<10 min" Av="10-20 min" Sd="20-30 min" DNF="30+ min" %}-->

## Setup

  * `mkdir hw4_uLogin`
  * `cd hw4_uLogin`
  * `touch bye.py convert.py fun.py string.py`

*Don't forget to add a comment at the top of each program with your name and what the program does.*

## bye.py

3. Edit the file (`ped bye.py`):
    4. Create a variable to store your last name
    1. Print "Goodbye, ...!" and replace the ellipsis (...) with the variable that is storing your last name.
    1. Add a comment at the top of the file that explains what your program does.
4. Run your python program: `python3 bye.py`
4. Copy your python file `bye.py` to `byebye.py`.

## convert.py

Create a program `convert.py`, that takes a fahrenheit temperature as input and outputs the equivalent temperature in celsius. Your program should have 2 variables:

  * `degrees_f`: holds a temperature in degrees fahrenheit (input from the user)
  * `degrees_c`: holds the temperature in degrees celsius. To convert fahrenheit to celsius, deduct 32 from the fahrenheit temperature and multiply by 5/9.

Your program shold print the values of both variables with a string description, such as: `"F degrees fahrenheit = C degrees celsius"`, replacing F & C with the values of your variables.

For example:

| **degrees_f** | **degrees_c** | **output** |
|---|---|
| 86 | 30 | 86 degrees fahrenheit = 30 degrees celsius |
| 72 | 22 | 72 degrees fahrenheit = 22 degrees celsius |
| 32 | 0 | 32 degrees fahrenheit = 0 degrees celsius |


## fun.py

Write a program `fun.py` that takes a number as input from the user and prints out the following information using the math module:

  1. The ceiling of the number (e.g., `ceiling(3.75)` is 4)
  1. The factorial of the number
  1. The number rounded to 0 decimal places

## string.py

Write a program `string.py` that takes a string as input form the user and prints the string after performing the following operations:

  1. Swaps upper and lower case letters
  1. Removes the second and second to last characters
  
Finally, print only the middle 3 letters using the substring or splice operation (`[:]`).
  
For example:

| **string** | **Mangled Output** | **Middle 3** |
|:---:|:---:|:---:|
| Monty Python | mNTY pYTHN | y P |
| hello | HLL | ell |


## Submission

Once you're satisfied that your programs are working correctly, zip it for submission:

  - `cd ..`
  - `zip hw4_uLogin.zip hw4_uLogin/*`

Upload your zip file to Google Classroom.
