# Demonstrate use of dictionary using ASCII values

# create an empty dictionary
ascii = {}

# See https://docs.python.org/3/library/functions.html#chr
# for an explanation of ord & chr
for x in range(ord('a'), ord('z') + 1):
    # add mapping to dictionary of chr(x) --> x (ordinal value)
    char = chr(x)
    ascii[char] = x

# order changes every run
print(ascii)

# Just sorted keys
# https://docs.python.org/3.4/library/functions.html#sorted
print(sorted(ascii))