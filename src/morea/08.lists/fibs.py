# Example of appending to a list
# Computes the first SIZE Fibonacci numbers

SIZE = 15

print("This program generates the first", SIZE, "Fibonacci numbers")

# create an empty list
fibs = []

# append the first two Fibonacci numbers
fibs.append(1)
fibs.append(1)

# compute the next 13 Fibonacci numbers
for x in range(2,SIZE):
    newfib = fibs[x-1]+fibs[x-2]
    fibs.append(newfib)


# print the Fibonacci numbers as a list
print(fibs)


# Tradeoff of using more space (the list) for easier implementation
