# Given a file of the form <lastname> <year>
# creates a mapping between the last names and years

FILENAME="data/years.dat"

# open the file for reading
yearsFile = open(FILENAME, "r")

lastNameToYear = {}

# read through each line of the file
for line in yearsFile:
    # split the line up into the parts, that were separated by white
    dataList = line.split()
    lastName = dataList[0]
    year = int(dataList[1]) # convert the data into an integer
    lastNameToYear[lastName] = year
    
yearsFile.close()

# Consider that we could use this to do a bunch of searches for students.
# For example, we could put this into a while loop

validStudent = False

while not validStudent:
    
    whichStudent = input("For which student's last name do you want to find out their graduation year? ")

    if whichStudent in lastNameToYear:
        print(whichStudent, "is expected to graduate in", lastNameToYear[whichStudent])
        validStudent = True
    else:
        print(whichStudent, "is not a student.")
        
        
