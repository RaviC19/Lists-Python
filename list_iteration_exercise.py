# write code that loops over the list and adds all the strings together to form one large combined string (no spaces between them)
# the combined string should be in all UPPERCASE
# save the result in a variable called result

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ""

for word in sounds:
    result += word.upper()

print(result)
