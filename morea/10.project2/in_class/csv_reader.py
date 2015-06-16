import csv

# Steps
# 1. print each line
# 2. print each item in each line
# 3. add all names to a set
# 4. create a friend dictionary of sets of friends
people = set()
with open('harry_potter.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		if(len(row) == 2):
			people.add(row[0])
			people.add(row[1])
			#print(row[0], ":", row[1])
		else:
			print("Malformed line:", row)

print(people)