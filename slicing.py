# Make new lists using slices of an old list
# some_list[start:end:step]
# start = what index to start slicing from
first_list = [1, 2, 3, 4]
first_list[1:]  # would return a new list of [2,3,4]
first_list[3:]  # would return a new list of [4]
first_list[-1:]
# entering a negative number will start the slice that many back from the end and in this case return [4]
first_list[-3:]  # would return [2,3,4]
first_list[:]  # would return the whole list of [1,2,3,4]

# end = the index to copy up to (exclusive like ranges)
first_list[:2]  # would return a new list of [1,2]
first_list[:4]  # would return a new list of [1,2,3,4]
first_list[1:3]  # would return a new list of [2,3]
# with negative numbers, how many items to exclude from the end(i.e indexing by counting backwards)
first_list[:-1]  # would return [1,2,3]
first_list[1:-1]  # would return [2,3]

# step = the number to count at a time, or the interval (like ranges). For example, a step of 2 counts every other number (1,3,5)
nums = [1, 2, 3, 4, 5, 6]
nums[1::2]  # would return [2,4,6]
nums[::2]  # would return [1,3,5]
# with negative numbers, reverse the order
nums[1::-1]  # would return [2,1]
nums[:1:-1]  # would return [6,5,4,3]
nums[2::-1]  # would return [3,2,1]

# reversing lists/strings
string = "This is fun"
string[::-1]  # returns 'nuf si sihT'

# modifying portions of lists
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ["a", "b", "c"]
# numbers is then returned as [1, 'a', 'b', 'c', 4, 5]

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colours[5]  # would return "indigo"
colours[5][::-1]  # would return "ogidni"

# Swapping values (useful when doing things like shuffling cards, sorting and algorithms)
names = ["Ravi", "Natsuki"]
names[0], names[1] = names[1], names[0]
print(names)  # would return ["Natsuki", "Ravi"]
