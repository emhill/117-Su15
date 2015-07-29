---
title: "PHW14"
published: true
morea_id: phw12
morea_type: experience
morea_sort_order: 14
morea_summary: "Final Exam Review"
morea_labels:

---

# Practice PHW14: Final Exam Review

<!--{% include wod-times.html Rx="<45 min" Av="45-90 min" Sd="90-135 min" DNF="135+ min" %}-->

## stat.py

Create a program `stat.py` that finds the mean, median, and mode in a list of numbers read in from a file `numbers.txt`. Do **not** use the python statistics package. Some definitions:

  * **mean**: the sum of the numbers divided by the number of numbers.
  * **median**: the middle number in a sorted list of numbers. If there is an even number of numbers, the median is the average of the middle two numbers.
  * **mode**: the most frequently occurring number.

***Recommended Development Steps:***

1. Instead of reading in from a file, create a list of numbers with `list(range(1,11))` and then `append(1)` to your list so you will have a mode. Print out the numbers.
2. Print out the mean for the list of numbers.
2. Print out the median for the list of numbers.
3. Print out the mode for the list of numbers.
4. Append another `1` to your list and print out the mean, median, and mode.
5. Read in a file `numbers.txt`, which should have a number entered one per line.
6. Write functions to read in the data from a file & calculate each statistic:
    * `file_input(filename)`: returns the list of numbers read in from file filename
    * `mean(numbers)`: takes a list of numbers as a parameter and returns their mean
    * `median(numbers)`: takes a list of numbers as a parameter and returns their median
    * `mode(numbers)`: takes a list of numbers as a parameter and returns their mode
 
***Hints:***

  * There are two different ways to sort a list: `sorted` and `sort`. The function `sorted(list)` returns a sorted version of the list without modifying the original, whereas `list.sort()` doesn't return anything but does change the original:
  
		>>> list = [5, 7, 5, 1, 5]
		>>> sorted(list)
		[1, 5, 5, 5, 7]
		>>> print(list)
		[5, 7, 5, 1, 5]
		>>> list.sort()
		>>> print(list)
		[1, 5, 5, 5, 7]

  * Make sure you don't have any blank lines in your file.

## Solution

When you've attempted the PHW, you can see my [solution](stat.py).

<!--
		
	def mean(numbers):
		return sum(numbers) / len(numbers)
	
	def median(numbers):
		sorted_num = sorted(numbers)
		if len(numbers) % 2 == 1: # odd
			return sorted_num[len(numbers) // 2]
		else: # even
			i1 = len(numbers) // 2 
			i2 = i1 - 1
			#print("i1:", i1, "i2", i2, "len:", len(numbers), sorted_num)
			return (sorted_num[i1] + sorted_num[i2]) / 2
	
	def mode(numbers):
		freq = {}
		for n in numbers:
			freq[n] = freq.get(n, 0) + 1
	# 		if n in freq:
	# 			freq[n] += 1
	# 		else:
	# 			freq[n] = 1
		#print(freq)
		mode = 0
		max = 0
		for key in freq:
			# freq.get(key) or freq[key]
			if freq.get(key) > max: 
				max = freq.get(key)
				mode = key
		return mode
	
	#numbers = list(range(1,11))
	numbers = []
	file = open("numbers.txt")
	for line in file:
		numbers.append(eval(line))
	file.close()
	
	print(numbers)
	print("Mean: ", mean(numbers) )
	print("Median: ", median(numbers) )
	print("Mode: ", mode(numbers) )-->