---
title: "PHW12"
published: true
morea_id: phw14
morea_type: experience
morea_sort_order: 19
morea_summary: "Objects in Python"
morea_labels:

---
# Practice HW12: Objects in Python

In this practice HW you will implement the `Date` class we began during lecture.

<!--{% include wod-times.html Rx="<45 min" Av="45-90 min" Sd="90-135 min" DNF="135+ min" %}-->

Begin by creating a file `date.py`:

	class Date:
	    """ a user-defined data structure that
	        stores and manipulates dates
	    """
	
	    # the constructor is always named __init__ !
	    def __init__(self, month, day, year):
	        """ the constructor for objects of type Date """
	        self.month = month
	        self.day = day
	        self.year = year
	
	
	    # the "printing" function is always named __repr__ !
	    def __repr__(self):
	        """ This method returns a string representation for the
	            object of type Date that calls it (named self).
	
	             ** Note that this _can_ be called explicitly, but
	                it more often is used implicitly via the print
	                statement or simply by expressing self's value.
	        """
	        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
	        return s
	
	
	    # here is an example of a "method" of the Date class:
	    def isLeapYear(self):
	        """ Returns True if the calling object is
	            in a leap year; False otherwise. """
	        if self.year % 400 == 0: return True
	        elif self.year % 100 == 0: return False
	        elif self.year % 4 == 0: return True
	        return False
	
## Understanding `Date`

 Notice that in this `Date` class there are three ***data members***:

* A data member holding the month (`self.month`)
* A data member holding the day of the month (`self.day`)
* A data member holding the year (`self.year`) 

Note that `self` is used to denote ***any*** object (that is, any variable or value) of class `Date`.


### Methods are just functions...

Object-oriented programming tends to have some of its own names for familiar things. For example, *method* is the "OOP" name for *function*. In particular, a *method* is a function whose first argument is `self`.

Note that the `Date` class has an `__init__` method and a `__repr__` method. As we've discussed in class, Python expects to see these special methods in virtually every class. The double underscores before and after these method names indicate that these methods are special ones that Python knows to look for. In the case of `__init__`, this is the method that Python looks for when making a new `Date` object. In the case of `__repr__`, this is the method that Python looks for when it needs to `repr`esent the object as a string.


Notice the line

    s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)

in the `repr` method. This constructs a string with the month, day, and the year, formatted very nicely to have exactly two digits places for the month, two digit places for the day, and four for the year.

We've also defined our own `isLeapYear` method. There are no double-underscores here, because Python didn't "expect" this method, but it certainly doesn't "object" to it either. (Clearly our puns have no *class*!)

### Note on "method":

Traditionally, functions called by objects are called *methods*. There is no really good reason for this. They are just like functions—-the only thing special about them is that they are defined in a class and they are called after a dot or period following the name of an object. For example, try these:

	>>> from date import *
	>>> d = Date(4, 7, 2015)
	>>> d.isLeapYear()
	False
	
	>>> d2 = Date(3, 15, 2016)
	>>> d2.isLeapYear()
	True
	
	>>> Date(1, 1, 1900).isLeapYear()   # no variable needed!
	False


### What's up with `self`?
One odd thing about the above example is that **three different objects** of type `Date` are calling the *same* `isLeapYear` code. How does the `isLeapYear` method tell the different objects apart? 

The method **does not** know the name of the variable that calls it! In fact, in the third example, there is *no* variable name! 

The answer is `self`. The `self` variable holds **the object that calls the method**, including all of its data members.

This is why `self` is always the first argument to all of the methods in the `Date` class (and in any class that you define): because `self` is how the method can access the individual data members in the object that called it.

**Please notice also:** this means that a method always has at least one argument, namely `self`. However, this value is passed in implicitly when the method is called. For example, `isLeapYear` is invoked in the example above as `Date(1,1,1900).isLeapYear()`, and Python automatically passed self, in this case the object `Date(1,1,1900)`, as the first argument to the `isLeapYear` method.

### Testing your initial `Date` class:

Just to get a feel for how to test your new datatype, try out the following calls:

	# create an object named d with the constructor
	>>> d = Date(4, 7, 2015)  # use another day if you prefer...
	
	# show d's value
	>>> d
	04/07/2015
	
	# a printing example
	>>> print 'Tuesday is', d
	Tuesday is 04/07/2015
	
	# create another object named d2
	# of *the same date*
	>>> d2 = Date(4, 7, 2015)
	
	# show its value
	>>> d2
	04/07/2015
	
	# are they the same?
	>>> d == d2
	False
	
	# look at their memory locations
	>>> id(d)   # return memory address
	413488      # your result will be different...
	
	>>> id(d2)  # again...
	430408      # and this should differ from above!
	
	# check if d2 is in a leap year...
	>>> d2.isLeapYear()
	False
	
	# yet another object of type Date
	# a distant New Year's Day
	# Q: where will you be on this date?
	>>> d3 = Date(1, 1, 2020)
	
	# check if d3 is in a leap year
	>>> d3.isLeapYear()
	True

### copy and equals

Add the following code to your `Date` class and then test that it works.

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

This `copy` method returns a newly constructed object of type Date with the same month, day, and year that the calling object has. Remember that the calling object is named self, so the calling object's month is `self.month`, the calling object's day is `self.day`, and so on.

Since you want to create a newly constructed object, you *need to call the constructor*. This is what you see happening in the copy method.

Try out these examples, which use next year's New Year's Day. First we don't use `copy`:

	>>> d = Date(1, 1, 2016)
	>>> d2 = d
	>>> id(d)
	430542      # your memory address may differ
	>>> id(d2)
	430542      # but d2 should be the SAME as d!
	>>> d == d2
	True           # so this should be True...


Next, you'll show that `copy` does make a deep copy (instead of a copy of only the reference, or "shallow" copy):
	
	>>> import date; reload(date); from date import *  # reload your file...
	>>> d = Date(1, 1, 2016)
	>>> d2 = d.copy()
	>>> d
	01/01/2016
	>>> d2
	01/01/2016
	
	>>> id(d)
	430568      # your memory address will differ
	>>> id(d2)
	413488      # but d2 should be different from d!
	>>> d == d2
	False         # thus, this should be false...


Next, add an `equals` method:

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

 This method should return `True` if the calling object (named `self`) and the argument (named `d2`) represent the same calendar date. If they do not represent the same calendar date, this method should return `False`. The examples above show that the same calendar date may be represented at multiple locations in memory—in that case the `==` operator returns `False`. This method can be used to see if two objects represent the same calendar date, regardless of whether they are at the same location in memory.

As a reminder, here is the line to reload a file without exiting Python:

	import date; reload(date); from date import *

Try these examples (after reloading date.py with the above line) to get the hang of how this equals method works.

	>>> d = Date(1, 1, 2016)
	>>> d2 = d.copy()
	>>> d
	01/01/2016
	>>> d2
	01/01/2016
	>>> d == d2
	False       # this should be False!
	
	>>> d.equals(d2)
	True        # but this should be True!
	
	>>> d.equals(Date(1, 1, 2016))  # this is OK, too!
	True
	
	>>> d == Date(1, 1, 2016)       # this tests memory addresses
	False                           # so it should be False


Now, the next part of the lab asks you to implement a few methods for the Date class from scratch.

## Modifications

Add the following methods to your `Date` class. Be sure to add a docstring to each of the methods you write. (Recall that the term method refers to a function that is a member of a user-defined class.)

### tomorrow(self)

This method should **NOT RETURN ANYTHING**. Rather, it should change the calling object so that it represents one calendar day after the date it originally represented. This means that `self.day` will definitely change. What's more, `self.month` and `self.year` might change.

Make sure to test your method with some tricky examples. Here are a couple of randomly chosen ones to get you started:

	>>> import date; reload(date); from date import *  # re-read file...
	
	>>> d = Date(12, 31, 2015)
	>>> d
	12/31/2015
	>>> d.tomorrow()
	>>> d
	01/01/2016
	
	>>> d = Date(2, 28, 2016)
	>>> d.tomorrow()
	>>> d
	02/29/2016
	>>> d.tomorrow()
	>>> d
	03/01/2016



### addNDays(self, N)

This method only needs to handle nonnegative integer arguments `N`. Like the `tomorrow` method, this method should not return anything. Rather, it should ***change*** the calling object so that it represents `N` calendar days *after* the date it originally represented. 

*Don't copy any code from the tomorrow method! **Instead***, consider how you could ***call*** the `tomorrow` method inside a `for` loop in order to implement this.

In addition, this method should *print* all of the dates from the starting date to the finishing date, inclusive of both endpoints. Remember that the line `print(self)` can be used to print an object from within one of that object's methods.

Make sure to test your method. Here are some to start with:

	>>> import date; reload(date); from date import *  # re-read file...
	
	>>> d = Date(4, 7, 2015)
	>>> d.addNDays(3)
	04/07/2015  # printing the first one is optional...
	04/08/2015
	04/09/2015
	04/10/2015
	>>> d
	04/10/2015
	
	>>> d = Date(4, 7, 2015)  # re-create this one
	>>> d.addNDays(1132)
	04/07/2015 
	04/08/2015
	... lots of dates skipped ...
	05/12/2018
	05/13/2018  
	>>> d
	05/13/2018    # graduation! (if you're now a first-year...)

You can check your own date arithmetic with this website: [http://www.timeanddate.com/date/dateadd.html](http://www.timeanddate.com/date/dateadd.html).

*Assignment adapted from [Harvey Mudd's CS 5 Virtual Art Lab](https://www.cs.hmc.edu/twiki/bin/view/CS5/Lab10).*

<!--## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="FMj6DvHxJw8" %}

{% include wod-warning.html %}-->

