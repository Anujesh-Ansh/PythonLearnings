# Exception Handling
# It is a way to handle errors in a program. It is used to handle the exceptions that can occur during the execution of a program.

# Syntax:
# try:
#     code to execute
# except:
#     code to execute if an exception occurs in the 'try' block
# else:
#     code to execute if no exceptions occur in the 'try' block
# finally:
#     code to execute regardless of whether an exception occurs or not

try:
    a = int (input("Enter a number: "))
    print(a)
except Exception as e:
    print("Invalid input:- ", e)