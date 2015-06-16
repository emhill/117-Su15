# Opens a file, reads it, and prints out its contents.


FILENAME="data/years.dat"

# creates a new file object, opening the file in read mode
myFile = open(FILENAME, "r")

# read the file and put it into one string
contents = myFile.read()

# close the file when you're done reading the file
myFile.close()

# display the contents of the file
print(contents, end="")

# To get the lines of the file from the contents, do
# lines = contents.split("\n")
