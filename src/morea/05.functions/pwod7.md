---
title: "PHW8"
published: true
morea_id: phw8
morea_type: experience
morea_sort_order: 7
morea_summary: "Go with the (control) flow"
morea_labels:
 - by 6/8
---
# Practice HW8: Go with the (control) flow

Rather than writing a program, in this practice HW you will walk through the execution of a program on paper. ***You don’t need to run the program to complete the assignment.***

<!--{% include wod-times.html Rx="<20 min" Av="20-40 min" Sd="40-60 min" DNF="60+ min" %}-->

## Exercise: loopy.py

Take a look at [loopy.py](loopy.pdf) and the output from a sample run. Each line of code in loopy.py is given a line number to the left. Given this sample run, in what order are the statements executed? List the line numbers in the order that they are executed. *Hint*: not all line numbers need to be included, and some line numbers may appear multiple times.

Make sure you can answer the following questions:

1. What is the first line executed?
1. What is the last line executed?
1. Is each function fruitful or void?

<!--## Demonstration

*Coming soon...*

Once you've finished doing the WOD a single time, you can watch me do it:

{% include youtube.html id="0BPlMXkwdcY" %}-->

<!--## Solution

Order that the lines are executed:

	34, 35, 36 get_area(+,+)
		5, 6, 7
	
	36, 38 rectangle_outline
		21, 22, 24, 25 draw_line(25)
			16, 25 * (17, 18), 19
	23 * (	22, 24, 28, 29, 23 * (30, 31), 32	)
		22, 24, 25 draw_line(25)
			16, 25 * (17, 18), 19 

	40 get_area(-,+)
		5, 6, 8, 9, 10, 11, 14

	41 get_area(+,-)
		5, 6, 8, 9, 10, 12, 13, 14

	43, 44 draw_line
		16, 17, 19
	43, 44, 16, 1 * (17, 18), 19
	43, 44, 16, 2 * (17, 18), 19
	43, 44, 16, 3 * (17, 18), 19
	43, 44, 16, 4 * (17, 18), 19
	43

Questions:

1. 34
1. 43 or 19
2. Fruitful or void?
    * get_area:		fruitful
	* draw_line:		void
	* rectangle_outline:	void

{% include wod-warning.html %}-->
