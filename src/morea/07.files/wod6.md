---
title: "WOD6: Data Structures & Files"
published: true
morea_id: wod6
morea_type: experience
morea_sort_order: 5
morea_summary: "In class"
morea_labels:
 - 4/13
---
# WOD6: Data Structures & Files


{% include wod-times.html Rx="<10 min" Av="10-20 min" Sd="20-30 min" DNF="30+ min" %}

### Setup

  * `mkdir wod6_uLogin`
  * `cd wod6_uLogin`
  * `touch vowels.py sort_sum.py`

*Don't forget to add a comment at the top of the program with your name and what the program does.*

## vowels.py
<!-- 5 min -->

Write a program `vowels.py` that declares the following set:

`letters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}`

and creates a simple dictionary with two keys, vowel & consonant, that stores the set of vowels and the set of consonants from the above set of letters. You should **not** manually create the set of consonants. Print out your dictionary to the file `letters.txt`.

Your program should also print the following (**NOT** to the file):

  1. A random sample of 3 letters
  1. The union of vowels & consonants
  1. The intersection of consonants and vowels

## sort_sum.py

Write a program `sort_sum.py` that allows the user to enter in a list of numbers, prints them out in sorted order, and prints the sum of the numbers. Prompt the user to continue entering numbers, and enter the number '0' when finished. You should use a list to store the numbers.

### Submission

Once you're satisfied that your programs are working correctly, zip it for submission:

  * `cd ..`
  * `zip wod6_uLogin.zip wod6_uLogin/*`


<!-- Started @ 11:20 -->