#task 1
# for i in range(1, 11):
#     print(i)

#task 2
# for i in range(2, 21, 2):
#     print(i)

#task 3
# for i in range(1, 21, 2):
#     print(i)

#task 4
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is", factorial)

#task 5
# total = 0
# for i in range(1, 101):
#     total += i
# print("Sum of numbers from 1 to 100 is", total)

#task 6
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# average = total / len(numbers)
# print("Average:", average)

#task 7
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#task 8
# for i in range(1, 6):
#      print(i)

#task 9
# for i in range(1, 11):
#      print(i)

#task 10
# numbers = [10, 20, 30, 40, 10]
# if numbers[0] == numbers[-1]:
#     print(True)
# else:
#     print(False)

#task 11
# numbers = [10, 23, 45, 66, 75, 90]
# for num in numbers:
#     if num % 5 == 0:
#         print(num)

#task 12
# char = input("Enter a character: ").lower()
# if len(char) == 1:
#     if char in 'aeiou':
#         print(f"Output: {char} is a vowel.")
#     elif char.isalpha():
#         print(f"Output: {char} is a consonant.")
#     else:
#         print("Output: Invalid input. Please enter an alphabet character.")
# else:
#     print("Output: Invalid input. Please enter a single character.")

#Task 13
# even_count = 0
# odd_count = 0
# for i in range(10, 56):
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even numbers count:", even_count)
# print("Odd numbers count:", odd_count)

#task 14
# for i in range(1, 26):
#     if i % 5 != 0:
#         print(i, end=' ')

#task 15
# numbers = [3, 4, 5]  # You can change this list
# for num in numbers:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"Factorial of {num} is {factorial}")

#task 16
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# product = a * b
# if product > 500:
#     result = a + b
# else:
#     result = product

# print("Result:", result)

#task 17
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print(f"{a} is greater.")
# elif b > a:
#     print(f"{b} is greater.")
# else:
#     print("Both numbers are equal.")

#task 18
# numbers = [12, -7, 5, -3, 8, -1]  # Example list
# positive = []
# negative = []
# for num in numbers:
#     if num >= 0:
#         positive.append(num)
#     else:
#         negative.append(num)
# print("Positive numbers:", positive)
# print("Negative numbers:", negative)

#task 19
char = input("Enter a character: ").lower()
if len(char) == 1:
    if char in 'aeiou':
        print(f"Output: {char} is a vowel.")
    elif char.isalpha():
        print(f"Output: {char} is a consonant.")
    else:
        print("Output: Invalid input. Please enter an alphabet character.")
else:
    print("Output: Invalid input. Please enter a single character.")