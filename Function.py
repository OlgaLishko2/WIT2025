
# #write a function that takes in the user's name and return
# #whether the length of the name is even or odd.
#
#
# def name_length (name):
#     # name = input('Your name: ')
#     # if len(name) % 2 == 0:
#     #     print('Even')
#     # else:
#     #     print('Odd')
#     return 'even' if len(name) % 2 == 0 else 'odd'
# print(name_length("ola"))



#create a list of dictionaries called employee it should have
# name, department, salary.
# write a function that returns the employee with the highest Salary


employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 52000},
    {'name': 'Bob', 'department': 'Engineering', 'salary': 85000},
    {'name': 'Charlie', 'department': 'Marketing', 'salary': 62000}
]

def highest_salary(result):

    return max(result, key=lambda e: e['salary'])

top_employee = highest_salary(employees)
print(top_employee)


# Write a program that find the factorial of a number
def factorial_loop(n):
    result = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial_loop(5))

# Write a  Python function to check whether a number falls within a given range.



#Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12




#Write a  Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5] - input list
#Unique List : [1, 2, 3, 4, 5]  - output list
