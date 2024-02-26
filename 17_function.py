# # Functions
# Functions are reusable blocks of code that can be called with a set of arguments. 
# They allow us to perform specific tasks without having to rewrite the same code over and over again. 
# Functions are defined using the def keyword, followed by the function name and a set of parentheses. 
# The function body is indented and contains the code to be executed when the function is called. 
# Functions can take parameters and return values. They can also have default parameter values and variable numbers of arguments. 
# Functions are called using the function name followed by a set of parentheses containing the arguments. 
# The return value of a function can be assigned to a variable or used directly in the code. 
# Functions can be defined inside other functions, and can be passed as arguments to other functions. 
# Functions can also be defined using the lambda keyword, which creates anonymous functions. 
# These functions are often used as arguments to other functions, or to create simple functions without having to define them using the def keyword. 
# Functions are a fundamental concept in programming, and are used to organize code, make it more readable, and reduce redundancy. 
# They are an essential part of any programming language, and are used in almost every program. 
# Functions are a powerful tool for creating modular, reusable code, and are an important part of any programmer's toolkit.

# # Syntax:
# def function_name(parameter1, parameter2, ...):
    # code to execute
#     return value

# Example: A simple addition function.
def add(a, b):
    return a + b

print(add(3, 4))  # Output: 7

# # Types of Functions

# Function definition with no parameters and no return value.
def greet():
    print("Hello!")

greet()  # Output: Hello

# Function definition with parameters and return value.
def greet(name):
    return f"Hello {name}!"

print(greet("Alice"))  # Output: Hello Alice!

# Function definition with default parameter value.
def say_hello(name, language="English"):
    return f"Hello {name}! Speak {language}?"

print(say_hello("Bob", "French"))  # Output: Hello Bob! Speak French?

# Function definition with variable number of arguments.
def count_args(*args):
    return len(args)

print(count_args(1, 2, 3))  # Output: 3