# Demonstrate use of dictionary using ASCII values

# create an empty dictionary
ascii = {}

# See https://docs.python.org/3/library/functions.html#chr
# for an explanation of ord & chr
for x in range(ord('a'), ord('z') + 1):
    # add mapping to dictionary of chr(x) --> x (ordinal value)
    char = chr(x)
    ascii[char] = x

# iterates through the keys in the dictionary
for letter in ascii:
    # print the key and its associated value
    print(letter, ascii[letter])

# display the type that is returned by dictionary methods
print(type(ascii.keys()))
print(type(ascii.values()))
print("The number of keys is", len(ascii))

# iterate through the values
print("Iterate through the values:")
for val in ascii.values():
    print(val)
    
keyList = list(ascii.keys())
print("as <dict_keys>:\n", ascii.keys())
print("as a list:\n", keyList)

# printing in order by key
keysSorted = list(ascii.keys())
keysSorted.sort()

print("Iterate through the values in order:")
for letter in keysSorted:  # alternative: sorted(keysSorted)
    # print the key and its associated value
    print(letter, ascii[letter])

print("Iterate through the values in order:")    
for letter in sorted(ascii):
    print(letter, ascii[letter])

