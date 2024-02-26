# Match Case
# The match case statement is used to compare the value of an expression to a pattern and execute the corresponding block of code.

# Syntax:
# match expression:
#   case value1, ...:
#     body1
#     ...
#   case valueN:
#     bodyN
# If no cases match the given expression, a ValueError is raised. The first matching case's body is executed and the rest are ignored.

a = int(input('Enter a number: '))

match a:
    case 5:
        print('a is equal to 5')
    case x if x > 5:
        print(f'{a} is greater than 5')
    case _:  # The default case
        print('a is less than 5')