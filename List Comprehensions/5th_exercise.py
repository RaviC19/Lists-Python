# Using a nested list comprehension and range(), create a variable called answer with the following value
# [[0,1,2], [0,1,2], [0,1,2]]
# To break it down, start by using range and a list comp to generate the list [0,1,2]
# Then repeat that whole thing 3 times in a nested list comp

answer = [[num for num in range(0, 3)] for val in range(0, 3)]
print(answer)
