# import math
# print(math.pi)
# import requests
# response = requests.get('https://api.github.com')
# print(response.status_code)

# import numpy as np
# print(np.array([1, 2, 3]))

# from math import pi, sqrt
# print(pi)
# print(sqrt(16))

# from math import sqrt as s, pi as p
# print(s(16))
# print(p)

# from math import * # wild card
# print(sin(90))  # Output: 0.0

# This is a global function because it's defined at the top level of the module.
# def my_function():
#   print("Hello! World")

# my_function()

# import random
# print(random.random())
 
# User-defined functions
# def my_function():
#   print("Hello! Operation Badar")

# my_function()

# def greetings():
#    "This is docstring of greetings function"
#    greet = 'Hello World!'
#    return greet

# message = greetings()
# print(message)

# def modify_value(x):
#     x = 10
#     print("Within function:", x)

# # Immutable object (integer)
# x = 5
# print("Original:", x)
# modify_value(x)
# print("After function:", x)

# def modify_list(lst):
#     lst.append(4)
#     print("Within function: ", lst, " - ID:", id(lst))

# # Mutable object (list)
# lst = [1, 2, 3]
# print("Original:", lst, " - ID:", id(lst))
# modify_list(lst)
# print("After function:", lst, " - ID:", id(lst))

# def greetings(name):
#    "This is docstring of greetings function"
#    print ("Hello {}".format(name))
#    return

# greetings("Anas")
# greetings("Omar")
# greetings("Uzair")

# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return;

# # Now you can call printinfo function
# printinfo( age=20, name="Anas" )
#printinfo(50, "Arif" )

# def add(x: int,y: int=0) -> float:
#    return float(x + y)

# print(float(add(10,20)))

# print(add(y=50.0, x=2.0)) # type hints are not enforced in Python

# print(add(x=5))

# def my_sum(*nums):
#   print(type(nums),", ", nums)

#   return sum(nums)

# print("Sum     = ", my_sum(1,2,3,4,5,8,5),"\n")
# print("Sum *[] = ", my_sum(*[1,2,3,4,5,8,5]), "\n") # *  unpacking list
# print("Sum *() = ", my_sum(*(1,2,3,4,5,8,5))) # *  unpacking tuple


# def printinfo( name, age = 20 ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return;

# # Now you can call printinfo function
# printinfo( age=20, name="Umar" )
# printinfo( name="Anas" )

# def posFun(x, y, /, z):
#     print(x + y + z)

# print("Evaluating positional-only arguments: ")
# posFun(1, 2, z=3)

# uncomment to see error
# posFun(x=1, y=2, z=3)

# def posFun(*, num1, num2, num3):
#     print(num1 * num2 * num3)

# print("Evaluating keyword-only arguments: ")
# posFun(num1=6, num2=8, num3=5)

# posFun(num3=6, num1=8, num2=5)

# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print ("Output is: ")
#    print (arg1)
#    for var in vartuple:
#       print ("*",var)
#    return;

# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50, 70, 90 )

# def add(x,y):
#    z=x+y
#    return z

# a=10
# b=20
# result = add(a,b)

# print ("a = {} b = {} a+b = {}".format(a, b, result))

# def add_two(x, y):
#   return x + y

# my_lambda = lambda x, y:  x + y;

# print(my_lambda(1,2))

# prompt: sort by value dictionary using lambda function
# prompt: sort by value dictionary using lambda function

# my_dict = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}

# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# print(sorted_dict)

# Function definition is here
# sum = lambda arg1, arg2: arg1 + arg2;

# # Now you can call sum as a function
# print ("Value of total : ", sum( 10, 20 ))
# print ("Value of total : ", sum( 50, 20 ))

from typing import Dict, List, Tuple


total = 0; # This is global variable.
# Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2; # Here total is local variable.
#    print ("Inside the function local total : ", total)
#    return total;

# # Now you can call sum function
# sum( 10, 20 );
# print ("Outside the function global total : ", total)

# def my_function(**student):
#   print("\nHis last name is " + student["lname"])

#   for key, value in student.items():
#     print(key, value)

#   print(student)

# my_function(fname = "Tariq Ali", lname = "Anas")

# my_function(fname = "Tariq Ali", lname = "Omar", course = "Inter", day="free with all times", time="free with all time")

# my_dict = {"fname": "Tariq Ali", "lname": "Uzair", "course":"Sarmaya", "day":"All Days", "time":"24 hours"}

# #my_function(my_dict) # uncomment to see TypeError
# my_function(**my_dict) # use ** to unpack the dictionary

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# # Create a generator object
# gen = simple_generator()

# print(gen, " : ", type(gen))

# # Iterate over the generator
# for value in gen:
#     print(value, " : ", type(value))

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num # Since yield pauses execution, it remembers the state and resumes from there when next() is called.
#         num += 1

# # Create a generator object
# gen = infinite_sequence() #initializes the generator.

# # Print the first 5 numbers, _ is a throw away variable
# for _ in range(5):
#     print(next(gen)) # The next time we call next(gen), execution resumes from where it left off.

# def infinite_loop(): #without yield it become infinite
#    num = 0
#    while True:
#        #yield num   # with yield it become generator without yield its a infinite loop
#        num += 1
#        print("infinite_loop() : num = ", num)

# infinite_loop()

# Generator expression
# gen = (x * x for x in range(5))
# print(type(gen))

# # Iterate over the generator
# for value in gen:
#     print(value, " : ", type(value))

# def factorial(n):
#     # Base case
#     if n == 0:
#         return 1
#     # Recursive case
#     else:
#         return n * factorial(n - 1)

# # Example usage
# print(factorial(5))  # Output: 120

# def fibonacci(n):
#     # Base cases
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Recursive case
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Example usage
# print(fibonacci(6))  # Output: 8

# prompt: generate an example of recursive function

# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)

# number = 5
# result = factorial(number)
# print(f"The factorial of {number} is {result}")

def example_function(a: int, b: int = 0, *args: float, **kwargs: str) -> Tuple[int, List[float], Dict[str, str]]:
    """Example function demonstrating various parameter types.
    Args:
        a: An integer.
        b: An integer with a default value of 0.
        *args: Variable-length positional arguments of type float.
        **kwargs: Variable-length keyword arguments of type string.
    Returns:
        A tuple containing:
        - The sum of 'a' and 'b'.
        - A list of the variable-length positional arguments ('args').
        - A dictionary of the variable-length keyword arguments ('kwargs').
    """
    sum_ab = a + b
    args_list = list(args)  # Convert tuple to a list
    return sum_ab, args_list, kwargs

# Example usage
result = example_function(1, 2, 3.14, 2.71, name="Alice", city="New York")
print(result)

result = example_function(10, *[1.0, 2.0, 3.0], **{"country": "USA", "language": "English"})
print(result)