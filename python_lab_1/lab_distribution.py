'''N student takes k apples and
distribute with them evenly
The remaining part remains in the basket
.How many apples get by each student?
How many apples will remains in the basket?
the program reads the numbers N and K.
It should print the two ans for the above question
'''
Number=float(input("Enter the number of students in class:"))
Apple=float(input("Enter the numbers of apples:"))
div=(Apple/Number)
rem=(Apple%Number)
print("Each student get",div)
print("remaining apples are",rem)






