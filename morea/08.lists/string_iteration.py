# Iterating through strings

phrase = input("Enter a phrase: ")

print("Iterate through phrase, using characters:")

for char in phrase:
    print(char)
    
print()

print("Iterate through phrase, using positions of characters:")
for pos in range(len(phrase)):
    print(pos, phrase[pos])
