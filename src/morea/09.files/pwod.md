---
title: "PHW10"
published: true
morea_id: phw10
morea_type: experience
morea_sort_order: 10
morea_summary: "Files & While"
morea_labels:

---
# Practice HW10: Files & While

In this practice HW you will create 3 programs that get input/output from files and use while loops. 

{% include wod-times.html Rx="<15 min" Av="15-30 min" Sd="30-45 min" DNF="45+ min" %}

## while.py

Create a program `while.py` that allows the user to enter in a list of numbers, prints them out in sorted order, and prints the sum of the numbers. Prompt the user to continue entering numbers, and enter the number ‘0’ when finished.

***Hints:***

* The [python `sum` function](https://docs.python.org/3/library/functions.html#sum) allows you to sum a list of numbers.
* I recommend following the sentinel while loop pattern:

      value = initialize
      while value != sentinel:
        process value
        value = updated value


## count.py

Write a program `count.py` that reads in [the file `turing.txt`](data/turing.txt) and counts the number of occurrences of the word "the". 

***Hints:***

  * Lowercase your words so that "the" is counted the same as "The".
  * Using one of the following functions is recommended:
    * The [string `split` function](https://docs.python.org/3.4/library/stdtypes.html#str.split) allows you to split a line of input into a list of words by splitting the line on spaces.
    * The [`count` function](http://www.thehelloworldprogram.com/python/python-string-methods/) allows you to count the number of occurrences in a string or list.
  * Review the lecture slides or example file programs in the unit for help on reading in a file, and [see this online tutorial](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)

***Recommended Development Steps:***

1. Download [`turing.txt`](data/turing.txt) & put it in the same folder as `count.py`.
2. Read in the file & print it out (either line by line or as one big string)
3. Print out the number of 'the's using the count function, **OR** complete the following steps.
4. Print the line split on spaces.
5. Print just a word on each line.
6. Only print out "the".
7. Count the number of times you see "the" (create a variable or a list) and print it out.

## lines.py

Write a python program that reads 3 files, called `text1.txt`, `text2.txt`, and `text3.txt`, counts the number of lines in each file, and prints out the number of lines to a file `counts.txt`. Each line of `counts.txt` should look like `[filename]: [the number of lines in the file]`.

***Hints:***

  * In UNIX you can get the number of lines in a file using the word count command: `wc -l [filename]`. This will allow you to test that your code is working correctly.
  * You should add the file names `text1.txt`, `text2.txt`, and `text3.txt` to a list, so you don't have to copy & paste your code.

<!--## Demonstration


Once you've finished doing the HW a single time, you can watch me do it for `while.py` and `count.py`:

{% include youtube.html id="2GkDAxZOnt8" %}

{% include wod-warning.html %}-->

