# Example illustrating list operations: concatenation and iteration

weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekendDays = ["Sat", "Sun"]

# combine two lists into one
daysOfWeek = weekDays + weekendDays

print("The Days of the Week:")

# iterate through elements of list
for day in daysOfWeek:
    print(day)

print("\nAGAIN!")

# iterate through positions of list
for x in range(len(daysOfWeek)):
    print(daysOfWeek[x])

print()  
# reorganizing days of week to start on a Sunday
daysOfWeek = weekendDays[-1:] + weekDays + weekendDays[:1]

extractWeekend = daysOfWeek[:1] + daysOfWeek[-1:]
print("Extracted weekend: ", extractWeekend)

extractWeekend2 = [daysOfWeek[0], daysOfWeek[-1]]
print("Extracted weekend: ", extractWeekend2)

notExtractedWeekend = daysOfWeek[0] + daysOfWeek[-1]
print("Does not work: ", notExtractedWeekend)
#notExtractedWeekend = [daysOfWeek[0]] + [daysOfWeek[-1]]
