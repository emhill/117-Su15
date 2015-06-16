FILENAME="data/years.dat"

dataFile = open(FILENAME, "r")

line = dataFile.readline()

while line != "":
    line = line.rstrip()
    print(line)
    line = dataFile.readline()

dataFile.close()
