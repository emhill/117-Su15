---
title: "PHW7"
published: true
morea_id: phw7
morea_type: experience
morea_sort_order: 6
morea_summary: "Functions: Putting it all together"
morea_labels:
 - by 6/4
---
# Practice HW7: Functions

In this practice HW you will create 5 programs that take code we've previously written for other PHWs and turn them into functions.

{% include wod-times.html Rx="<20 min" Av="20-40 min" Sd="40-60 min" DNF="60+ min" %}

## hello_function.py

Write a function `hello` which takes a name as a parameter and prints "Hello, ...", replacing the ellipsis (...) with the parameter. Test your function by asking the user for their name.

## tip_calculator.py

Recall `tip.py` from [PHW3]({{site.baseurl}}/morea/04.python/pwod3.html). Copy `tip.py` into `tip_calculator.py`. Modify it by creating a function `calculate_total` that takes 3 parameters and returns the total for the meal. The 3 parameters are:

  * `meal`: the cost of the meal
  * `tax_rate`: the percent tax. For example, NJ tax would be 0.07.
  * `tip_rate`: the percent tip. A 20% tip rate would be 0.20.

Use the same calculations as in the prior lab (NOT the CodeAcademy exercise). Specifically, proper tipping technique dictates that the tip should be calculated based on the total cost of the meal, before tax is applied. Then, print out the total with 2 decimal places. Don’t forget the dollar sign ($)!

Prompt the user to enter the cost of the meal, the tax rate, and the tip rate. Your final program should make two calls to `calculate_total`: one based on input from the user and one using the following call:

    calculate_total(53.48, .07, .18)

*Note that the total for the above meal with tax & tip is $66.85.*

## absolute_value.py

Write a function `absolute_value` that takes a number as a parameter and returns its absolute value without using any python functions (in other words, you should use an if statement not `abs`). Test that your function works by calling it twice, once with a positive and once with a negative number, and printing the results. *Your program should **not** get any input from the user.*

## is_multiple.py

Write a function `is_multiple` that takes a number and a multiple as parameters and returns true if the number is a multiple (i.e., if `number % multiple` is 0). Test that your function works by calling it twice, once with a multiple and once with a number that is not its multiple, and print the results. *Your program should **not** get any input from the user.*

## rectangle.py

Create a program that draws a filled rectangle of asterix characters, requesting the width and height from the user. Write a function `rectangle` that takes the number of rows and columns (i.e, height & width) as parameters. If the width or height entered by the user is less than 1, the function prints an informative error message. Otherwise, the function prints the filled rectangle. Make sure to test your program with positive and negative values for width & height. *Hint:* you may find the [`loop_fun.py` example from class](https://drive.google.com/a/drew.edu/file/d/0B46T_IyJH_ovLWpObFZkLXdsM0U/view?usp=sharing) (part C, using 2 loops) to be helpful.

## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="0BPlMXkwdcY" %}

{% include wod-warning.html %}
