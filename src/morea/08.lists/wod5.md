---
title: "WOD5: Recursion, Strings, & Lists"
published: true
morea_id: wod5
morea_type: experience
morea_sort_order: 5
morea_summary: "In class"
morea_labels:
 - 3/27
---
# WOD5: Recursion, Strings, & Lists


{% include wod-times.html Rx="<10 min" Av="10-20 min" Sd="20-30 min" DNF="30+ min" %}

### Setup

  * `mkdir wod5_uLogin`
  * `cd wod5_uLogin`
  * `touch mangle.py sum.py count.py`

*Don't forget to add a comment at the top of the program with your name and what the program does.*

## mangle.py

Write a function `mangle` that takes a string as a parameter and returns the string after performing the following operations:

  1. converting the string to all upper case letters
  1. removing any digits
  1. removing the last character
  
For example:

| **string** | **mangle(string)** |
|---|---|
| hello9 | HELL |
| 42 degrees Celsius | DEGREES CELSIU |

Test your program by calling the mangle function & printing its results on at least 3 example strings. *Your program should **not** get any input from the user.*

## sum.py

Create a program that calculates the sum of a list of 5 numbers entered by the user. Make sure you ask (i.e., prompt) the user to enter each number (the user will hit enter after each number). You should use the python [sum](https://docs.python.org/3/library/functions.html#sum) function.

## count.py

Write a `count_a` function which takes a word as a parameter and returns the number of times the letter 'A' or 'a' appears in that string. For full credit you should use recursion or list comprehensions. Partial credit for using a loop. Test your function by getting user input.

### Submission

Once you're satisfied that your programs are working correctly, zip it for submission:

  * `cd ..`
  * `zip wod5_uLogin.zip wod5_uLogin/*`


<!-- Started @ 11:20 -->