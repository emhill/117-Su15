# Given a file of the form <lastname> <year>
# creates a mapping between the years and the number of students.


FILENAME="data/years.dat"

# open the file for reading
yearsFile = open(FILENAME, "r")

yearToCount = {}

# read through each line of the file
for line in yearsFile:
    # split the line up into the parts, that were separated by white
    dataList = line.split()
    # convert the year into an integer
    year = int(dataList[1])
    # if the year is already in the dictionary 
    #  --> I already have a counter for that year.
    if year in yearToCount:
        yearToCount[year] += 1
    # this is the first time I'm seeing that year.
    else:
        yearToCount[year] = 1
    
yearsFile.close()

print("A summary of the class year and the number of students in that year:")
print("Year Count")
print("----------")
for year in sorted(yearToCount):
    print("%4s %5d"% (year, yearToCount[year]))
    
