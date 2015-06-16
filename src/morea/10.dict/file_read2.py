# Opens a file, reads the file one line at a time, and prints the
# contents


FILENAME="data/years.dat"

# creates a new file object, opening the file in "read" mode
dataFile = open(FILENAME, "r")

# reads in the file line-by-line and prints the content of the file
for line in dataFile:
    # remove the newline character from the line
    line = line[:-1]
    # didn't use rstrip method in case want to preserve trailing
    # spaces from the original file
    print(line)

# close the file with the method "close"
dataFile.close()
