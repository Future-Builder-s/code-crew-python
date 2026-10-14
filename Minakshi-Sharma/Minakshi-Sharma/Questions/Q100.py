#Q100. Create your own small real-world data record and write a program that demonstrates variable creation, reassignment, type inspection, and multiple valid type conversions without using any topic outside this lecture.

name = "Minakshi Sharma"
college_name = "IIT MADRAS"
level = "Foundation"
term = 2
marks = 500 

print(name,type(name))
print(college_name,type(college_name))
print(level,type(level))
print(term,type(term))
print(marks,type(marks))

print("-"*30)

name = "Anshika Mittal"
print(name,type(name))
marks = "Five hundred"
print(marks,type(marks))
level = "Diploma"
print(level,type(level))
marks = int(marks)
print(marks,type(marks))
