---
title: "HW"
published: true
morea_id: phw6
morea_type: experience
morea_sort_order: 5
morea_summary: "Functions"
morea_labels:

---
# HW: Functions


<!--{% include wod-times.html Rx="<5 min" Av="5-10 min" Sd="10-20 min" DNF="20+ min" %}-->

{% include wod-times.html Rx="<20 min" Av="20-40 min" Sd="40-60 min" DNF="60+ min" %}

## is_multiple.py

Write a function `is_multiple` that takes a number and a multiple as parameters and returns true if the number is a multiple (i.e., if `number % multiple` is 0). Test that your function works by calling it twice, once with a multiple and once with a number that is not its multiple, and print the results. *Your program should **not** get any input from the user.*

For example:

| **call** | **returns** |
|:---:|:---:|
| `is_multiple(10, 5)` | True | 
| `is_multiple(10, 7)` | False | 
| `is_multiple(8, 4)` | True | 
| `is_multiple(8, 3)` | False | 


## tip_calculator.py

Recall `tip.py` from [PHW3]({{site.baseurl}}/morea/04.python/pwod3.html). Copy `tip.py` into `tip_calculator.py`. Modify it by creating a function `calculate_total` that takes 3 parameters and returns the total for the meal. The 3 parameters are:

  * `meal`: the cost of the meal
  * `tax_rate`: the percent tax. For example, NJ tax would be 0.07.
  * `tip_rate`: the percent tip. A 20% tip rate would be 0.20.

Use the same calculations as in the prior practice HW (NOT the CodeAcademy exercise). Specifically, proper tipping technique dictates that the tip should be calculated based on the total cost of the meal, before tax is applied. Then, print out the total with 2 decimal places. Don’t forget the dollar sign ($)!

Prompt the user to enter the cost of the meal, the tax rate, and the tip rate. Your final program should make two calls to `calculate_total`: one based on input from the user and one using the following call:

    calculate_total(53.48, .07, .18)

*Note that the total for the above meal with tax & tip is $66.85.*

<!--## is_odd.py

Write a function `is_odd` that takes a number as a parameter and returns true if the number is odd. Test that your function works by calling it twice, once with an odd and once with an even number. *Your program should **not** get any input from the user.*-->

## rectangle.py

Create a program that draws a filled rectangle of asterix characters, **requesting the width and height from the user**. Write a function `rectangle` that takes the width & height as parameters and prints a filled rectangle.

For example, a call to `rectangle(3,5)` should output:

    ***
    ***
    ***
    ***
    ***

<!--### Submission

Once you're satisfied that your programs are working correctly, take a screenshot of each program open in the editor, with its output displayed in the console, and submit to google classroom. You should submit 3 screenshots.-->


<!-- Started @ 11:35 -->

## Select Solutions

<!--The solutions below are to the right. Scroll over to see them!
--><!-- Highlight them or copy/paste to see them!-->

Keep scrolling down if you're sure you want to see the solutions!
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>

### is_multiple.py
   
    def is_multiple(num, m):
      return num % m == 0

    print(is_multiple(5))
    print(is_multiple(6))

<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>

### rectangle.py

    def rectangle(w, h):
      for i in range(h):
         print(w * "*")
    
    width = eval(input("Enter width: "))
    height = eval(input("Enter height: "))
    rectangle(width, height)

<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>
<BR>