# Writes content from a user to a file


PROMPT = "Enter the next line in the file: "

outfilename = input("What is the name of your output file? ")
numLines = eval(input("How many lines do you want to write? "))

# create a new file object, in "write" mode
dataFile = open(outfilename, "w")

for x in range(numLines):
    userinput = input(PROMPT)
    # write the user's input to the file
    dataFile.write(userinput)
    # write a newline after each input from the user
    dataFile.write("\n")

# close the file with the method "close"
dataFile.close()
