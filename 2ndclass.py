import keyword
print(keyword.kwlist)

#Example of taking input from the user
name=input("Enter your name: ")
age=input("Enter your age: ")
print("your name is: ",name)
print("your age is: ",age)
print(name)
print(age)
###taking two numbefr from the user and adding them
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
sum_result=num1+num2
print(f"the sum of{num1} and {num2} is {sum_result}")

# Taking bacis information 
student_name = input("Enter the Student's name: ")
student_age = input("Enter the Student's age: ")
student_class = input("Enter the Student's class: ")

# taking mark 
math_mark = float(input("Enter the annual mark for Math: "))
english_mark = float(input("Enter the annual mark for English: "))
science_mark = float(input("Enter the annual mark for Science: "))

# calculate marks 
total_marks = math_mark + english_mark + science_mark
average_marks = total_marks / 3

# Displaying the number
print("\nStudent Information")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Class: {student_class}")
print("\nMarks Information")
print(f"Math: {math_mark}")
print(f"English: {english_mark}")
print(f"Science: {science_mark}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
# new program
x=int(input('enter the value of x: '))
y=int(input('enter the value of y: '))
z=int(input('enter the value of z: '))
equation=x*x*x + x*x*y - z*z*z
print(f"the result is {equation}")
