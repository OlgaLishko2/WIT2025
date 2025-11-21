# greet = 'Hello world'
# print(greet)

# for i in range(2, 12):  # range stops before 12
#     print(i)
# for i in range(2, 12, 3):  # start at 2, stop before 12, step 3
#     print(i)
# fib = [1, 2]  # start with the first two numbers

# while len(fib) < 7:  # we want 7 numbers total
#     fib.append(fib[-1] + fib[-2])  # sum of last two numbers

# for num in fib:
#     print(num)

# #Task 1
# values = []

# val1 = input("Enter the first value: ")
# val2 = input("Enter the second value: ")

# values.append(val1)
# values.append(val2)

# print("List of values:", values)

# # Task 2
# while True:
#     number = int(input("Enter a number between 10 and 50: "))
#     if 10 <= number <= 50:
#         print("You entered:", number)
#     break

# else:
#     print("Invalid input. Try again.")




# A police officer is looking for a criminal 
# # who named Sam, who is a 34 year old female.
# # Find the criminal from the suspectList

# suspectList = [{
#   'name': 'Sam',
#   'sex': 'Male',
#   'age': 21
# }, {
#   'name': 'John',
#   'sex': 'Male',
#   'age': 25
# }, {
#   'name': 'Sandra',
#   'sex': 'Female',
#   'age': 22
# }, {
#   'name': 'Sam',
#   'sex': 'Male',
#   'age': 34
# }, {
#   'name': 'Paula',
#   'sex': 'Female',
#   'age': 29
# }, {
#   'name': 'Sam',
#   'sex': 'Female',
#   'age': 34
# }]


# for suspect in suspectList:
#     if suspect['name'] == 'Sam' and suspect['sex'] == 'Female' and suspect['age'] == 34:
#         print("Criminal found:", suspect)
#     # else:
#     #     print("Criminal not found")


# Write an if statement that prints “>” if first number is larger than second number, “<” if first number is smaller than second number, == if they are equal.

# first_num = input("First number: ")
# second_num = input("Second number: ")

# if first_num > second_num:
#     print('>')
# elif first_num < second_num:
#     print('<')
# elif first_num == second_num:
#     print('==')


# There is a list of integers [2, 6, 1, 5, 9, 4, 10, 3, 8, 7].
# Write a program where it takes an integer input(grater than 0) from the user and prints out all the numbers in the list which are smaller than the user input.
# i.e. If the user typed an integer 5, the output should be 2 1 4 3. (separate line or same line, but in the same order from the list)


# integers = [2, 6, 1, 5, 9, 4, 10, 3, 8, 7]
# new_list = []
# num = int(input("Enter an integer greater than 0: "))

# while num <= 0:
#     print("Please enter a number greater than 0.")
#     num = int(input("Enter an integer greater than 0: "))
# for i in integers:

#     if i < num:
#         new_list += [i]

# print(new_list)


# There is a list of integers [2, 6, 1, 5, 9, 4, 10, 3, 8, 7].  Write a program where it prints out the sum of the elements inside the list.


# integers_list = [2, 6, 1, 5, 9, 4, 10, 3, 8, 7]
# print(sum(integers_list))


# When a year is given, write a program that prints 1 if the year is leap year, and prints 0 otherwise.
# You can tell that it is a leap year, when the year is multiple of 4, AND is not multiple of 100 or is multiple of 400.
# For example, 2012 is a multiple of 4, and not a multiple of 100, so it is a leap year.
# 1900 is a multiple of 100, and not a multiple of 400, so it is not a leap year.
# 2000 is a multiple of 400, so it is a leap year.
# 1 < year < 4000
# Sample Input A: 2000
# Sample Output A: 1
# Sample Input B: 1999
# Sample Output B: 0

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('Leap year')
# else:
#       print('Not Leap year')



# You’re teaching math in high school and you need a program to enter students’ grades based on their exam score. Write a program that takes 
# a score of student’s math exam, and prints a proper grade based on the following rule:
# * type(score) = int
# A: 90~100
# B: 80~89
# C: 70~79
# D: 60~69
# F: ~59


score = int(input("Enter exam score: "))
if 100 >= score >= 90:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('E')