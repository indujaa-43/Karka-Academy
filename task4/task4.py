# Task:1
# num = float(input("Enter a number: "))
# if num > 0:
#     print("The number is Positive.")
# elif num < 0:
#     print("The number is Negative.")
# else:
#     print("The number is Zero.")

# Task 2: 
# num = int(input("Enter an integer: "))
# if num % 2 == 0:
#     print("The number is Even.")
# else:
#     print("The number is Odd.")    

# Task 3: 
# base = int(input("Enter the base number: "))
# exponent = int(input("Enter the exponent: "))
# result = base ** exponent
# print("Result:", result)

# Task 4: 
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# if num1 > num2:
#     print("The first number is greater.")
# elif num2 > num1:
#     print("The second number is greater.")
# else:
#     print("Both numbers are equal.")

# Task 5: 
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a Leap Year.")
# else:
#     print(year, "is Not a Leap Year.")

# Grade Calculator Program

#task 6:
score = int(input("Enter the student's score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
elif score < 60:
    grade = 'F'
else:
    grade = 'Invalid score'
print("Grade:", grade)



# Task 7: 
# age = int(input("Enter your age: "))
# if age < 16:
#     print("You can't drive.")
# elif age >= 16 and age <= 17:
#     print("You can drive but not vote.")
# elif age >= 18 and age <= 24:
#     print("You can vote but not rent a car.")
# else:
#     print("You can do pretty much anything.")


#Task 8: 
# for num in range(1,10):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# Task 9:
# print("Python Programming Task Practice - 4\n")
# year = int(input("Enter the year = "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")        