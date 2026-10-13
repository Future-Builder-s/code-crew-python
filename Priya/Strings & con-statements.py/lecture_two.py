#str1 = "This is a String.\twe are creating it in python."
#print(str1)

#length of str
str2 = "apna"
len1 = len(str2)
print(len1)


str3 = "college"
len2 = len(str3)
print(len2)

final_str = str2 + " "+ str3
print(final_str)
print(len(final_str))

#indexing
str = "apna college"
ch = str[0]
print(ch)

#slicing
str1 = "Apna College"
print(str1[1:4])
print(str1[5:12])
print(str1[:12])


#String Functions
str = "i am learning Python from Apna College"
print(str.endswith("ege"))      
print(str.capitalize())         

str4 = "apna college"
print(str4.replace("e","a"))     
print(str4.find("o"))            
print(str4.count("apna"))        


#Conditional Statements
#if condition:
age = 21

if(age >= 18): 
    print("can vote & apply for license")
    print("can drive")

#elif condition:
light = "yellow"

if(light == "red"):
    print("stop")

elif(light == "green"):
    print("go")

elif(light == "yellow"):
    print("look")

#else condition
age = 14
if(age >= 18):
    print("CAN VOTE")
else:
    print("CANNOT VOTE") #indentation

#example

marks = 74
if(marks >= 90):
    grade = "A"

elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the students ->",grade)

#example

#marks = int(input("enter students marks: "))
#if(marks >= 90):
    #grade = "A"

#elif(marks >= 80 and marks < 90):
    #grade = "B"
#elif(marks >= 70 and marks < 80):
    #grade = "C"
#else:
    #grade = "D"

#print("grade of the students ->",grade)

#nesting
age = 95
if (age >= 18):
    if (age >= 80):
        print("CANNOT DRIVE")
    else:
        print("CAN DRIVE")
else:
    print("CANNOT DRIVE")            







