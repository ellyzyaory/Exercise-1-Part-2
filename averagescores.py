print("Student scores: ")
mark1 = eval(input(" "))
while mark1 < 0:
    print("Student scores: ")
    mark1 = eval(input(" "))
mark2 = eval(input(" "))
while mark2 < 0:
    print("Student scores: ")
    mark1 = eval(input(" "))
    mark2 = eval(input(" "))
mark3 = eval(input(" "))
while mark3 < 0:
    print("Student scores: ")
    mark1 = eval(input(" "))
    mark2 = eval(input(" "))
    mark3 = eval(input(" "))

average = (mark1 + mark2 + mark3)/3

print("Average: ", average)
