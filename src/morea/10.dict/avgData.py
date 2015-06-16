# Computes the average high temperature from a file that contains the daily
# high temperatures for last year at one location.


import sys

DATAFILE="data/alaska.dat"

# open the file
tempFile = open(DATAFILE, "r")

# read the data file
contents = tempFile.read()
tempFile.close()

# break the contents up by line
tempStrList = contents.split()

# Alternative way to find out how many temperatures are in the file
#altNumTemps = len(tempStrList)

# initialize the accumulators
tempTotal = 0
numTemps = 0

# iterate over the temperatures, which are strings
for tempStr in tempStrList:
    # need to convert the string to a float
    temp = float(tempStr)
    # accumulate the temperature total and the number of temperatures
    tempTotal += temp
    numTemps += 1

# Check to make sure we have the correct number of temperatures.
if numTemps != 365:
    print("Please check", DATAFILE)
    print("It does not seem to have the right number of temperatures in it.")
    sys.exit(1)

# compute the average
average = tempTotal/numTemps

# display the average...
print("The average high temperature from %s is %.2f" % (DATAFILE, average))
