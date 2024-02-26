# If Else Statement
# The if statement is used to check a condition. If the condition is true, a block of code is executed. Otherwise, another block of code can be executed using the else statement.

# Syntax:
# if condition:
#     code block if true
# else:
#     code block if false

x = int(input("Enter a number: "))
if x > 5:
    print('x is greater than 5')
else:
    print('x is less than 5')   

# The elif keyword is used to specify multiple conditions. It is similar to else if in other programming languages.
    
# Syntax: 
# if condition1:
#     code block if true
# elif condition2:
#     code block if true
# else:
#     code block if all conditions are false
    

if x == 5:
    print('x is equal to 5')
elif x > 5:
    print('x is greater than 5')
else:
    print('x is less than 5')  
