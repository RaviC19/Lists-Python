# Given a list ["Ellie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list
# Although could loop over manually, use a list comprehension

names = ["Ellie", "Tim", "Matt"]
answer = [char[0] for char in names]
print(answer)

# Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.
numbers = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)

# Clearer answers
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]
