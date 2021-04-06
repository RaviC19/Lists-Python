# Create a list called instructors
# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
# Remove the last value in the list
# Remove the first value in the list
# Add the string "Done" to the beginning of the list

instructors = []
instructors.extend(["Colt", "Blue", "Lisa"])
instructors.pop()
instructors.pop(0)
instructors.insert(0, "Done")

print(instructors)
