# Given a file containing students names and their years (freshman, sophomore,
# junior, or senior) for this class, creates a report (in a file) that
# says the year and how many students from that year are in this class, on the
# same line.


FILENAME="data/years.dat"
REPORTNAME="data/report.dat"

print("This program finds out how many students of each class year are")
print("enrolled in the class and writes that information to a file.")
print()
print("Reading file", FILENAME)
print("Writing report to", REPORTNAME)


# what we're looking for:
classYears = ["FIRST-YEAR", "SOPHOMORE", "JUNIOR", "SENIOR"]
# accumulator list
classYearCounts = [0]*4

# read the input file 
fileObj = open(FILENAME, "r")
contents = fileObj.read()
fileObj.close()

# when we split the content, we're getting a list of students, 
# represented as strings
studentInfoList = contents.split()

# calculate the number of students per year

for whichYear in range(len(classYears)):
    for studentInfo in studentInfoList:
        if classYears[whichYear] in studentInfo:
            classYearCounts[whichYear] += 1

# check the counts for the class year to make sure that the counts are correct
#print(classYearCounts)

# Write the info we found in the last step into the report file
reportFile = open(REPORTNAME, "w")

for whichYear in range(len(classYears)):
    className = classYears[whichYear]
    classCount = classYearCounts[whichYear]
    
    # since we need to write a string to the file, 
    # it's often easier to write a formatted string to the file
    reportFile.write( "%s %d\n" % (className, classCount))
    
    # alternative:
    # reportFile.write(className + " " + str(classCount) + "\n")
    
reportFile.close()
