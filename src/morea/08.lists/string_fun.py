# Fun with strings
# 09.15.14
# Emily Hill
# CSCI 117

##################################
# PRINTING
##################################

"""Basic printing with a variable"""
name = "Monty"

"""puts spaces @ each"""
print("My name is", name, ".")

"""use + to control your own spaces:"""
#print("My name is " + name + ".")

"""alternative to remove spaces is a format string:"""
#print("My name is--%s." % name)

"""What if I want to use double quotes?"""
#print("My name is "%s"." % name)
#print("Escape is needed for newline,\n\t tabs and \\.")
#print('\tAnd sometimes \'.')

##################################
# STRING FUNCTIONS
##################################

series = "MONTY python's flYinG ciRCus"

#print(series)
#print(series.upper())
#print(series.lower())
#print(series.title())

"""
See https://docs.python.org/3.4/library/functions.html#len
http://www.python-course.eu/python3_formatted_output.php
"""
#print("Series title has %d characters" % len(series))

##################################
# STRING AS A LIST OF CHARACTERS
##################################

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY PYTHON"[4]

#print(fifth_letter)

##################################
# MATH FUNCTIONS
##################################

"""
https://docs.python.org/3/library/math.html
To use a math function, you need to IMPORT it:
"""

#import math
#print("The square root of 100 is", math.sqrt(100))

"""
To use just one, like square root
https://docs.python.org/3/library/math.html#math.sqrt
and not type 'math' in front all the time:
"""

#from math import sqrt
#print("The square root of 25 is", sqrt(25))

""" What will be output? """
#print(10  / 3)
#print(10  % 3)
#print(10 ** 3)

"""
Let's clean up the output:
http://www.python-course.eu/python3_formatted_output.php
"""
#print("%8.2f\n%8.2f\n%8.2f" % (10/3, 10%3, 10**3))

##################################
# GET INPUT FROM THE USER
##################################

"""
Let's get some input from the user.
In Python 2 (CodeAcademy) we would use the function raw_input
In Python 3 (python3) we use input():
https://docs.python.org/3/library/functions.html#input
"""

#name = input("What is your name? ")
#os   = input("What is your operating system (OS)? ")
#print("Hey %s, %s users rock!" % (name, os))
