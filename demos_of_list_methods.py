# Define a list called my_stuff which must be atleast 4 elements long and contain atleast 1 string and 1 float
my_stuff = ["Ravi", 3.40, "Snooker", 2]

# Define a list called nums which contains all the numbers between 1 and 99
nums = list(range(1, 100))
print(nums)

# Using a for loop to access all the values in a list
numbers = [1, 3, 4, 55, 78, 1323]
for num in numbers:
    print(num)

# Using a while loop to access all the values in a list
colours = ["red", "white", "black", "brown", "yellow", "orange", "pink"]
index = 0
while index < len(colours):
    print(f"{index}: {colours[index]}")
    index += 1

# Add one value to the end of a list
cities = ["Toyko", "London", "Barcelona"]
cities.append("Kotor")

# Add multiple values to the end of a list
years = [1990, 1991, 1992]
years.extend([1993, 1997, 1966, 1967, 2002])
print(years)

# Insert an item at a given position
num_list = [1, 2, 3, 4]
# First number in the below .insert is the index where the value will be added
num_list.insert(1, "Two")
print(num_list)

# To add something to the end of the list
num_list.insert(len(num_list), "Last number")
print(num_list)

# To remove all items from the list
num_list.clear()
print(num_list)

# Remove a item at a given position in the list and return it
first_list = [1, 2, 3, 4, 5]
first_list.pop(1)
# If no index is specified, the last item in the list is removed and returned
first_list.pop()

# Remove the first item from the last that matches the value you are trying to remove. Error thrown if item is not found
teams = ["Man Utd", "Man City", "Chelsea",
         "Liverpool", "Arsenal", "Tottenham", "Man City", "Everton"]
teams.remove("Chelsea")
print(teams)

# Return the index of a specified item in a list
teams.index("Tottenham")  # Would return 5
# Can specify start and end
teams.index("Man City", 1)
# Looks for "Man City" between the indexes of 2 and 7
teams.index("Man City", 2, 7)
# Return the number of times a value appears in the list
teams.count("Man City")
# Reverse the elements of the list
teams.reverse()
# Sort the items of the list (in ascending order)
teams.sort()
print(teams)

# .join is techincally a string method but commonly used with lists
# concatenates a copy of the base string between each item of the iterable and then returns a new string
words = ["I", "am", "learning", "Python"]
" ".join(words)
# Would return a string "I am learning Python"
