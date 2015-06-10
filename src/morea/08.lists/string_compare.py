# Program compares two strings

str1 = input("Enter a string to compare: ")
str2 = input("Compare '" + str1 + "' with what string? ")

print("-" * 40)

if str1 < str2 :
    print("Alphabetically,", str1, "comes before", str2 + ".")
elif str1 > str2:
    print("Alphabetically,", str2, "comes before", str1 + ".")
else:
    print("You tried to trick me!", str1, "and", str2, "are the same word!")


print(str1 * 4)