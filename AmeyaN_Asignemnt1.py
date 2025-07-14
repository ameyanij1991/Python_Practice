#Author - Ameya Nijasure - AICTE ID - 1-2905050722
#Assignment 01 - Introduction to Python and Data structures

#Program 01 - Program to find greater of three numbers
a = input("Enter first number - a :") #take value of a
b = input("Enter second number - b :") #take valur of b
c = input("Enter third number - c :") #take value of c

#using if and elif to find the greatest number

if a>=b and a>=c:  
    #checking Condition for a with b and c
    greatest = a

elif b>=a and b>=c:
    #checking Condition for b with a and c
    greatest = b   

else:
    #If both fails C is greatest number
    greatest = c   

#Print the result
print("The greatest number is:",greatest)

#Program 02 - Program to find given number is even or odd

#taking user input as interger for arithmatic operations
x = int(input("Enter any number x :"))

#using if and modulus operator (reminder) to check number is even or odd
if x % 2 == 0:
    #if reminder is zero - number is even    
    print ("x is even number , x = ",x) 
else:
    #if reminder is zero - number is odd
    print ("x is odd number , x = ",x)  

#Program 03 - Program to check a year is a leap year or not

#taking interger value as user input - requirement for Arithmatic operators
year_input = int(input("Enter a year: ")) 

# Check leap year conditions
if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
    print(f"{year_input} is a Leap Year")
else:
    print(f"{year_input} is NOT a Leap Year")

# Program 04 - Simulation of Traffic Signal
# Take input from user
colour = input("Enter traffic signal color (red / yellow / green): ")
# Convert to lowercase for uniform comparison in if condition
colour = colour.lower()

# Using if-elif-else to decide action
if colour == "green":
    print("Signal is GREEN: Go")
elif colour == "red":
    print("Signal is RED: Stop")
elif colour == "yellow":
    print("Signal is YELLOW: Slow down")
else:
    print("Signal is BROKEN")

# Program 05 - Program to calculate Grade of a student
# Take makrs obtained by student from user
grade = int(input("Enter grade obtained by :"))
if grade >= 90:
    #Condition for grade A
    print("Grade obtained by studuent is A")
elif grade > 80 and grade < 89:
    #Condition for grade B
    print("Grade obtained by studuent is B")
elif grade > 70 and grade < 79:
    #Condition for grade C
    print("Grade obtained by studuent is C")
elif grade > 60 and grade < 69:
    #Condition for grade D
    print("Grade obtained by studuent is D")
elif grade > 50 and grade < 59:
    #Condition for grade E
    print("Grade obtained by studuent is E")
else:
    #Below 50 Student Fails
    print("Student is Failed")