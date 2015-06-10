from statistics import mode

numbers = []
#numbers = [1, 2, 5, 5, 5]
for x in range(5):
  #num = x
  num = input("Please enter number: ")
  numbers.append(num)
  #numbers = numbers + [num]

print(mode(numbers))