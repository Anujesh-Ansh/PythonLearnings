# Indentation
# Python uses indentation to define code blocks, instead of brackets. The standard indentation requires standard 4 spaces.

# Example:
def func():
    print('Line 1')
    print('Line 2')
    
func()  

# Output: Line 1
#         Line 2


# But now:
def func():
    print('Line 1')
print('Line 2')
    
func()  

# Output: Line 2
#         Line 1

# Explanation of the difference:
# In the first example, "print('Line 2')" is a part of the function, and is executed after the function is called.
# In the second  example, 'print(" Line 2")' is not a part of the function, and is executed before the function is called.

# This is because, the print('Line 2') is not indented, and therefore, it is not a part of the function, and is executed before the function is called.