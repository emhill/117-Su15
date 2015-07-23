---
title: "PHW8"
published: true
morea_id: phw8
morea_type: experience
morea_sort_order: 8
morea_summary: "Recursion & Lists"
morea_labels:

---
# Practice HW8: Recursion & Lists

In this practice HW you will create 3 programs that use strings, lists, and recursion.

{% include wod-times.html Rx="<30 min" Av="30-60 min" Sd="60-90 min" DNF="90+ min" %}

## mode.py

Create a program that calculates the most frequently occurring number in a list of 10 numbers. You may hard-code in a list of numbers rather than getting them as input from the user. You may use the python [mode](https://docs.python.org/3.4/library/statistics.html#statistics.mode) function from the statistics package.

***Recommended Development Steps:***

1. Create a list of 10 numbers and print it out
2. Make sure one number occurs more than any other
2. Print out the [mode](https://docs.python.org/3.4/library/statistics.html#statistics.mode) function applied to the list

## wheel.py

Write an **iterative** function `count_vowels` which takes a word as a parameter and returns the number of vowels in that string.

Write a **recursive** function `sajak` which takes a word as a parameter and returns the number of vowels in that string.

Test both functions by asking the user to enter a word, and printing the number of vowels found by each function.

***Recommended Development Steps:***

1. Create a variable containing a single letter. Write an if statement to determine if that letter is a vowel or not. (***Hint***: use `in`)
2. Put that if inside a loop that iterates through every letter in a string and prints out whether each letter is a vowel or not
3. Update the loop to count the number of vowels and print the total at the end. This is the `count_vowels` function.
4. For the recursive `sajak` function, think about how you can recursively print the first or last letter in a string, and implement it.
5. Instead of printing the letter, print whether it's a vowel.
6. Instead of printing, count whether the letter is a vowel or not.

## text.py

Write a function `pyramid` that takes a string of text as a parameter and outputs the text as follows:

    Enter text: we love CS
	w
	we
	we 
	we l
	we lo
	we lov
	we love
	we love 
	we love C
	we love CS
	we love C
	we love 
	we love
	we lov
	we lo
	we l
	we 
	we
	w

You may use *either* recursion *or* iteration in your solution. Note: if you use recursion, will need to implement 2 functions: one for printing top triangle of letters and one that prints the bottom triangle of letters. If using iteration, you will need 2 loops.

Test your functions by getting a string of text from the user and printing the results of both functions.

***Recommended Development Steps:***

1. Create a string variable & print it out
1. Think about the pattern of strings that are printed. Write a loop or a recursive function that successively prints out a substring from index 0 to the end. (***Hint***: use `:`)
2. Now print the other way
3. Get input from the user

<!--## Demonstration


Once you've finished doing the HW a single time, you can watch me do it. ***Note***, this video includes exercises in a different order:

{% include youtube.html id="hsjv5f2DlFk" %}

Recursive solution to pyramid function in `text.py`:

{% include youtube.html id="yBrjRTtFiTE" %}

{% include wod-warning.html %}-->

