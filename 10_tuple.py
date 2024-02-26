# Tuple
# Tuple is a collection of items which is ordered and unchangeable. Allows duplicate members.

# Example:
# Creating a tuple ->
x = (1, 2, 'Anujesh', 4, 5)
print(type(x))                     # Output: <class 'tuple'>

x[2] = 'Ansh'                   # Error because tuple is immutable

# Output: 'tuple' object does not support item assignment

y = ('a', 'b', 'c')                # A tuple with string elements
z = (10, 20, 30, 40, 50)           # A tuple with integer elements
print(z)

print(len(y), y)                   # Output: 3 ('a', 'b', 'c')
print(len(z), z)                # Output: 5 (10, 20, 30, 40, 50)

# Accessing the element in tuple using indexing
print(y[0], y[-1])                 # Output: a c
print(z[1], z[-2])                 # Output: 20 40

# Slicing in tuple
print(y[:2], y[1:])                # Output: ('a', 'b') ('b', 'c')
print(z[:3], z[2:])                # Output: (10, 20, 30) (30, 40, 50)

# Check if an item exists in the tuple
if 'Anujesh' in y:
    print('Anujesh is present in the tuple')
else:
    print('Anujesh is not present in the tuple')

# Check membership using "in" operator
print(10 in z)                     # Output: True
print(60 in z)                    # Output: False

# Check for equality of tuples
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)

print(t1 == t2)                    # Output: True
print(t1 == t3)                # Output: False  # Tuple is a collection of items which is ordered and unchangeable. Allows duplicate members.