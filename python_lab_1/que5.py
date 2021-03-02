'''a school decidesd to replace the desk in three classrooms.Each desk sits two student
Given the number of each class, print the smallest possible number of desk that can be purchased
.the program should read three integers:the number of student in each of three classes a,b,c respectively
In the first there are three groups.The first group has 20 students and thus needs 10 desk
the second group has 21 students, so they can get by with no fewer then 11 desk.
11 desk are also enough
for the third group of 22 students.so, we need 32 desk in total.
'''
no_student_class1=int(input("Enter the number of student in first class :"))
no_student_class2=int(input("Enter the number of student in 2nd class:"))
no_student_class3=int(input("Enter the number of student in third class:"))

desk_class1=(no_student_class1//2)
print("The required number of desk in class1 are :",desk_class1)
desk_class2=(no_student_class2//2)
print("The required number of desk in class2 are :",desk_class2)

desk_class3=(no_student_class3//2)
print("The required number of desk in class3 are :",desk_class3)



