# Example of creating a list of the appropriate size
# Computes the first SIZE Fibonacci numbers

SIZE = 15

print("This program generates the first", SIZE, "Fibonacci numbers")

# creates a list of size 15, containing numbers 0-15
fibs = list(range(SIZE))
# alternative: create list of size 15, all containing 0s: [0]*15

fibs[0] = 1
fibs[1] = 1

for x in range(2, len(fibs)):
    newfib = fibs[x-1]+fibs[x-2]
    fibs[x] = newfib

print(fibs)

# To print out the list, each element on a separate line
#for num in fibs:
#    print num
