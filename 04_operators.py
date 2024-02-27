# Operators
# Operators are special symbols in Python that carry out arithmetic or logical computation. They perform actions on one or more values and return a result.

# Types of Operators:
# Assignment Operators: =, +=, -=, *=, /=, //=, **=, %=, >>=, <<=, &=, ^=, |=
# Arithmetic Operators: +, -, *, /, //, %, **
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Bitwise operators: &, | , ~, ^, <<, >>

# Assignment Operators
num1 = 5                   # Simple Assignment
print(num1)
num1 += 3                  # Add AND Assignment
print(num1)


# Arithmetic Operators
print(3+4)  # Addition = 7
print(5-2)  # Subtraction = 3
print(9*8)  # Multiplication = 72
print(10/2)  # Division = 5.0
print(10//3)  # Floor Division = 3
print(10 % 3)  # Modulus = 1
print(2**3)  # Exponentiation = 8

# Comparison Operators
num = 5
print(num==7)   # False
print(num!=6)   # True
print(num>4)    # True
print(num<9)    # True
print(num>=6)   # True
print(num<=5)   # False

# Logical Operators
x = 5
y = 10
print(x==5 and y==10)   # True  (Both conditions are True)
print(x==5 or y==11)    # True  (Atleast one condition is True)
print(not x==5)         # False (Negation of True is False)

# Bitwise AND operator
a = 10
b = 4
print(a & b)     # 0    (Binary of 10 = 1010, Binary of 4 = 0100, Bitwise AND of 1010 and 0100 = 0000)

# Bitwise OR operator
print(a | b)      # 14  (Binary of 10 = 1010, Binary of 4 = 0100, Bitwise OR of 1010 and 0100 = 1110)

# Bitwise XOR operator
print(~a)        # -11  (Binary of 10 = 1010, Bitwise NOT of 1010 = 0101)
print(a^b)       # 14   (Binary of 10 = 1010, Binary of 4 = 0100, Bitwise XOR of 1010 and 0100 = 1110)

# Left Shift Operator
print(a<<2)      # 40   (Binary of 10 = 1010, Left Shift of 1010 by 2 = 101000)

# Right Shift Operator
print(a>>2)      # 2    (Binary of 10 = 1010, Right Shift of 1010 by 2 = 10)    (Right Shift of 1010 by 2 = 10)