#lists in python
marks1 = 98.5
marks2 = 88.0
marks3 = 72.9
marks4 = 47.5
marks5 = 66.7

marks = [98.5,88.0,72.9,47.5,66.7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))


#
student = ["karan",98.5,22,"delhi"]
print(student[0])
student[0] = "arjun"
print(student)

#list slicing
marks = [98.5,88.0,72.9,47.5,66.7]
print(marks[1:4])

#list methods

list = [2,1,3]    #append
list.append(4)
print(list)

list = [4,5,8,2,1]     #sort
print(list.sort())
print(list)

list = [4,5,8,2,1] 
print(list.sort(reverse=True)) #reverse
print(list)

list = [2,1,1,3]
list.pop(2)
print(list)        #remove

#tuple
tup = (2,1,3,2)
print(type(tup))

tup = (5,2,4,1)
print(tup[1:3])

tup = (2,4,5,1,3)
print(tup.index(2))


tup = (2,4,5,1,3)
print(tup.count(2))

#1 WAP to ask to user enter names of their favourite movie and store them in a list.
movie = []
movie1 = input("enter 1st movie: ")
movie2 = input("enter 2nd movie: ")
movie3 = input("enter 3rd movie: ")

movie.append(movie1)
movie.append(movie2)
movie.append(movie3)

print(movies)


