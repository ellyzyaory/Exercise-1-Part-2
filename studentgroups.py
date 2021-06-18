class1 = 32
class2 = 45
class3 = 51

print("Number of students in each group: ")

class1_group = int(input("Class 1: "))
while class1_group <= 0:
    class1_group = int(input("Class 1: "))
class2_group = int(input("Class 2: "))
while class2_group <= 0:
    class2_group = int(input("Class 2: "))
class3_group = int(input("Class 3: "))
while class3_group <= 0:
    class3_group = int(input("Class 3: "))

students_each_group1,class1_leftover = divmod(class1,class1_group)
students_each_group2,class2_leftover = divmod(class2,class2_group)
students_each_group3,class3_leftover = divmod(class3,class3_group)

print("Number of students in each group: ")
print("Class 1: ", students_each_group1)
print("Class 2: ", students_each_group2)
print("Class 3: ", students_each_group3)

print("Number of students leftover: ")
print("Class 1: ", class1_leftover)
print("Class 2: ", class2_leftover)
print("Class 3: ", class3_leftover)
