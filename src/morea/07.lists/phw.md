---
title: "PHW9"
published: true
morea_id: phw9
morea_type: experience
morea_sort_order: 18
morea_summary: "List Comprehensions"
morea_labels:

---
# Practice HW9: List Comprehensions

In this practice HW you will explore writing some list comprehensions.

{% include wod-times.html Rx="<5 min" Av="5-10 min" Sd="10-15 min" DNF="15+ min" %}

Write python code (as a program or in the python interpreter) that prints out the following using list comprehensions of the form:

    print([c for x in sequence])

where c is the computation and x is an element in a sequence. Remember that you can also put an `if` after the sequence to further restrict what elements are added to the list.

You should be able to print:

  * twelve 12's
  * the absolute values from -10 to 10
  * the even numbers from 0 to 100
  * the perfect squares from 0 to 100
  * the number of odd numbers in the range of 0 to 100
  * the number of vowels in the string "Hello, there!"


<!--## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="FMj6DvHxJw8" %}

{% include wod-warning.html %}-->

<!--## Solution

When you've attempted the PHW, you can see my solution below.

    >>> print([12 for x in range(12)])
    [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    
	>>> print([abs(x) for x in range(-10,11)])
	[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
	>>> print([x for x in range(101) if x % 2 == 0])
	[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
	
	>>> print([x**2 for x in range(1, 101) if x**2 < 100])
	[1, 4, 9, 16, 25, 36, 49, 64, 81]
	
	>>> print(sum([1 for x in range(101) if x % 2 == 1]))
	50
	
	>>> print(sum([1 for x in "Hello, there!" if x in "AEIOUaeiou"]))
	4-->