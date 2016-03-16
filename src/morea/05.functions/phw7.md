---
title: "HW"
published: true
morea_id: phw7
morea_type: experience
morea_sort_order: 7
morea_summary: "Recursion I"
morea_labels:

---
# HW: Recursion I

<!--In this practice HW you will create 2 programs that take code we've previously written for other PHWs and turn them into functions.-->

{% include wod-times.html Rx="<15 min" Av="15-30 min" Sd="30-45 min" DNF="45+ min" %}

## power.py

Write a function `power` which takes two numbers (`base` and `exponent`) as parameters and calculates the value `base ** exponent` using recursion by repeatedly multiplying `base`.

Next write a function `power_loop` which takes two numbers (`base` and `exponent`) as parameters and calculates the value `base ** exponent` using a loop.

Test that both functions return the same value when called with the same parameters. 

## steps.py

Write a function `text_steps` that takes a string as a parameter and recursively prints the text as follows:

    Enter text: CS@DREW rocks!
    CS@DREW rocks!
    S@DREW rocks!
    @DREW rocks!
    DREW rocks!
	REW rocks!
	EW rocks!
	W rocks!
	 rocks!
	rocks!
	ocks!
	cks!
	ks!
	s!
	!

Test your function works by getting a string as input from the user.

For extra practice, try writing `text_steps` using a loop instead of recursion.

<!--## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="nTb-SeIGMCM" %}

### Solution for `text_steps` loop:
    def step_loop(txt):
	    for i in range(len(txt)):
		    print(txt[i:])

{% include wod-warning.html %}-->

### Submission

Once you're satisfied that your programs are working correctly, take a screenshot of each program open in the editor, with its output displayed in the console, and submit to google classroom. You should submit 2 screenshots.
