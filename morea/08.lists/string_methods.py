# Manipulate strings, using methods

sentence = input("Enter a sentence to mangle: ")

length = len(sentence)

# Question: What does the statement below do?
print("*", sentence.center(int(length*1.5)), "*")

print("Uppercase: ", sentence.upper())
print()
print("Lowercase: ", sentence.lower())
print()

# Answer before running...
print("Did sentence change?: ", sentence)
