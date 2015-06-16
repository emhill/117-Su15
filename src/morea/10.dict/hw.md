---
title: "HW9"
published: true
morea_id: hw9
morea_type: experience
morea_sort_order: 10
morea_summary: "frequency.py"
morea_labels:

---
# HW9: Word Frequencies

Write a program `frequency.py` that reads in [the file `turing.txt`](data/turing.txt) and counts the number of occurrences of each word. Your program should print out these word occurrences in sorted order by decreasing frequency value. For example, "the" occurs 10 times and would be printed out before "Alan", which occurs just once.

Your program should not take in any user input, just read in the hard-coded filename `"turing.txt"`. You may use any example template to read in the file (for loop, while loop, etc).

***Recommended Development Steps:***

1. Read in the file & print it back out.
2. Read in the file, split each line on spaces, & print each word on a separate line.
    * To check your work, use the UNIX command `python3 frequency.py | sort | uniq -c | sort -rn` to give a list of all the words sorted by frequency. 
    * Make sure you don't see any unwanted values like punctuation or spaces. If you do, tweak your program to get your desired output. (See hints below.)
    * Your next step is to implmement the above UNIX command in your python program using a dictionary.
3. Create a frequency dictionary and add each word to it: `freq[word] = 1`. Print out the dictionary.
4. Count the number of words (see hints below). Print out the dictionary.
5. Sort the dictionary by values before printing. (See hints below.)

***Hints:***

  * The [string `split` function](https://docs.python.org/3.4/library/stdtypes.html#str.split) allows you to split a line of input into a list of words by splitting the line on spaces.
  * Lowercase your words so that "the" is counted the same as "The".
  * Don't forget to replace punctuation so "Alan" is counted the same as "Alan,". I recommend the [`replace` function](http://www.tutorialspoint.com/python/string_replace.htm) for this. You can use a loop on a string to replace many characters.  
  * When counting words with a dictionary, you may need to check if the word is in the dictionary already. If it is, just add 1 to the current value. If it's not, initialize it to 1. If you are using the `count` function you may not encounter this issue.
  * You can use the built-in [sorted function](https://wiki.python.org/moin/HowTo/Sorting/) to sort by values. The [`operator.itemgetter` function](https://docs.python.org/3/library/operator.html#operator.itemgetter) makes a good key. For more information, see [this answer on stack overflow](http://stackoverflow.com/a/613218)


<!--## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="FMj6DvHxJw8" %}

{% include wod-warning.html %}-->

