---
title: "PHW11"
published: true
morea_id: phw11
morea_type: experience
morea_sort_order: 15
morea_summary: "Dictionaries"
morea_labels:
 - by 6/17
---
# Practice HW11: Sets & Dictionaries

In this practice HW you will create 2 programs that use data structures (i.e., sets, lists, tuples, and dictionaries). ***Make sure to read the hints & recommended development steps for each program.***

{% include wod-times.html Rx="<10 min" Av="10-20 min" Sd="20-30 min" DNF="30+ min" %}

## sets.py

Create a program `sets.py` that declares the following set:

`s = {"A", "B", "C", "D", "E"}`

and prints a random element of the set until the first element is sampled. In other words, the while loop continues printing letters in the set `s` until "A" is the next letter. The output should have no "A"'s.

Then, create another set:

`r = {"A", "C", "E", "G"}`

and print the results of the following [set operations](https://docs.python.org/3.4/library/stdtypes.html#set): union, intersection, and difference.

***Hints:***

* The following code randomly selects an element from a set:

      import random            s = {"A", "B", "C", “D”, “E”}            print(random.sample(s, 1)) 
* For more information see the [random sample function](https://docs.python.org/3.4/library/random.html#random.sample).
 
* I recommend following the sentinel while loop pattern:

      value = initialize
      while value != sentinel:
        process value
        value = updated value

***Recommended Development Steps:***

1. Create the set `s` and print it out
2. Print out a random sample of 1 element from `s` instead (see hints above)
3. Use the sentinal template in the hints above to create a while loop that prints out a random letter until the value is "A"
4. Create the set `r` and print out the union with `s`
5. Print out the intersection and difference


## dictionary.py

Create a program `dictionary.py` that creates a simple dictionary with two keys, even & odd, that stores the **set** of even & odd numbers from 1 to 10 and prints it out.

***Hints:***

 * Use the [`set()` function](https://docs.python.org/3.4/library/stdtypes.html#set) to initialize an empty set.

***Recommended Development Steps:***

1. Write a loop that prints out the numbers from 1 to 10
2. In this loop, print out whether the number is even or odd
3. Create a set for even and a set for odd numbers. Instead of printing in the loop, add the number to the appropriate set. Print out the sets after the loop.
4. Replace your set variables by adding them to a dictionary `d` instead. For example, if you had a set named `even`, replace every occurrence of that variable with `d['even']`. Make sure you initialize `d` to be an empty dictionary (`d = {}`). Print out the dictionary after your loop to confirm the behavior is the same as in the prior step.


<!--## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="hogc3cXLbRU" %}

{% include wod-warning.html %}-->

