---
title: "HW"
published: true
morea_id: phw3
morea_type: experience
morea_sort_order: 5
morea_summary: "Input, Strings, and Using Functions"
morea_labels:

---
# HW: Input, Strings, and Using Functions

{% include wod-times.html Rx="<10 min" Av="10-20 min" Sd="20-30 min" DNF="30+ min" %}

## Setup

In PyCharm, create two python files: `maths.py` & `mangle.py`. <!--(If you've forgotten how to do that, refer back to [the previous HW](http://emhill.github.io/150/morea/01.unix/phw1.html).)-->

*Don't forget to add a comment at the top of each program with your name and what the program does.*

## maths.py

Write a program `maths.py` that takes a number as input from the user and prints out the following information using the math module:

  1. The floor of the number (e.g., `floor(3.75)` is 3)
  1. The absolute value of the number (this should be stored as a variable called `absolute_value`)
  1. The square root of `absolute_value` rounded to 2 decimal places <!-- factorial -->
  1. `absolute_value` times -1

## mangle.py

Write a program `mangle.py` that takes a string as input from the user and prints the string after performing the following operations:

  1. converting the string to all upper case letters
  1. removing the third character
  1. removing the third to last character
  
For example:

| **string** | **mangle(string)** |
|:---:|:---:|
| hellothere | HELOTHRE |
| 42 degrees Celsius | 42DEGREES CELSUS | 

**Hints:**

  * How do we convert a string to upper case? Try googling! You can also look at the slides & textbook readings.
  * How do we remove from strings using only slices (i.e., [:])?

<!--## Submission

Once you're satisfied that your programs are working correctly, take a screenshot of each program open in the editor, with its output displayed in the console, and submit to google classroom. You should submit 2 screenshots.-->

<!--## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="8uFbvxWgi9E" %}

{% include wod-warning.html %}-->
