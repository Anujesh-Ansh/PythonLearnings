# # TypeCasting
# is a process of converting one data type to another data type.

# # Typecasting in Python:
# 1. Implicit Type Casting - It happens automatically by python interpreter when we assign value of one data type to another.
# 2. Explicit Type Casting - It is done by user using predefined functions like int(), float(), str(), etc.

a = 3
print(a) # Output = 3 (Integer)

b = '3'
print(b) # Output = 3 (String)

# print(b+a) -> this would show error, because we cannot add a string and an integer directly. We need to convert the integer into a string, and then add them.
# therefore

print(int(b) + a) # Output = 6 (Integer)

# Similar examples:

c = 4.5
d = int(c)
print(d) # Output = 4 (Integer)

e = "10"
f = float(e)
print(f) # Output = 10.0 (Float)

g = True
h = int(g)
print(h) # Output = 1 (Integer)

i = False
j = int(i)
print(j) # Output = 0 (Integer)
