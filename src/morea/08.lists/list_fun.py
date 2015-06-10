# http://www.pythontutor.com/visualize.html#mode=edit

admins-MacBook-Pro-2:08.lists emily$ python3
Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 00:54:21) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> months = ["Jan", "Feb", 3, "Apr", "May", "JUNE"]
>>> months[1]
'Feb'
>>> months[2]
3
>>> months[0]
'Jan'
>>> len(months)
6
>>> months[5]
'JUNE'
>>> months[-1]
'JUNE'
>>> months[-2]
'May'
>>> months[1:2]
['Feb']
>>> months[1:3]
['Feb', 3]
>>> months[1:4]
['Feb', 3, 'Apr']
>>> months[1:4] * 3
['Feb', 3, 'Apr', 'Feb', 3, 'Apr', 'Feb', 3, 'Apr']
>>> months[0] * 12
'JanJanJanJanJanJanJanJanJanJanJanJan'
>>> months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
>>> print(months)
['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
>>> academic = months[8:] + months[:8]
>>> print(academic)
['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
>>> len(academic)
12
>>> "Aug" in months
True
>>> "Au" in months
False
>>> for i in academic:
...   print(i * 3)
... 
SepSepSep
OctOctOct
NovNovNov
DecDecDec
JanJanJan
FebFebFeb
MarMarMar
AprAprApr
MayMayMay
JunJunJun
JulJulJul
AugAugAug
>>> vector1 = [45, 60, 50]
>>> vector2 = [32, 45, 2000]
>>> for i in vector1:
...   print(i - vector2[0])
... 
13
28
18
>>> for i in range(3):
...   print( vector1[i] - vector2[i] )
... 
13
15
-1950
>>> daysOfWeek = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"] 
>>> daysOfWeek[0:-1]
['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
>>> daysOfWeek[0] daysOfWeek[]
KeyboardInterrupt
>>> daysOfWeek[0] + daysOfWeek[-1]
'SunSat'
>>> [daysOfWeek[0]] + [daysOfWeek[-1]]
['Sun', 'Sat']
>>> daysOfWeek[0:0] + daysOfWeek[-1:-1]
[]
>>> daysOfWeek[0:1] + daysOfWeek[-1:]
['Sun', 'Sat']
>>> daysOfWeek[1:5]
['Mon', 'Tues', 'Wed', 'Thurs']
>>> daysOfWeek[1:6]
['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
>>> daysOfWeek[1:-1]
['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
>>> (daysOfWeek[0:1] + daysOfWeek[-1:]) * 3
['Sun', 'Sat', 'Sun', 'Sat', 'Sun', 'Sat']
>>> week = daysOfWeek[0:1] + daysOfWeek[-1:]
>>> daysOfWeek[0:1] + daysOfWeek[-1:] = week
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> week * 3
['Sun', 'Sat', 'Sun', 'Sat', 'Sun', 'Sat']
>>> string = "hello"
>>> string.upper()
'HELLO'
>>> print(string)
hello
>>> string = string.upper()
>>> print(string)
HELLO
>>> daysOfWeek.reverse()
>>> print(daysOfWeek)
['Sat', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon', 'Sun']
>>> string[0] = 'u'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> daysOfWeek[0] = "HelloDay"
>>> print(daysOfWeek)
['HelloDay', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon', 'Sun']
>>> dow = daysOfWeek
>>> print(dow)
['HelloDay', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon', 'Sun']
>>> print(daysOfWeek)
['HelloDay', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon', 'Sun']
>>> dow[0] = "Saturday"
>>> print(dow)
['Saturday', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon', 'Sun']
>>> print(daysOfWeek)
['Saturday', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon', 'Sun']
>>> 
