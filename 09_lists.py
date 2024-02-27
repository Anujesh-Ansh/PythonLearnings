# List
# A list is a collection of items, which is ordered and changeable. In Python lists are written with square brackets.# This is a list of all the functions that can be performed on a list:

# Example:
# Creating a list ->

l1 = [1, 2, 8, 4, 5,'Ansh']

# Type
print(type(l1))

print(l1)

# Removing a particular element from the list
l1.remove('Ansh')
print(l1)

# Sorting the list, in ascending order, and updating the list itself
l1.sort()
print(l1)

# Sorting in Descending order
l1.sort(reverse=True)
print(l1)

# Removing the last most element from the list
l1.pop()
print(l1)

# Adding an element to the list
l1.append(6)
print(l1)

# Adding an element at a particular index
l1.insert(2, 3) # Insert 3 at index 2
print(l1)

# Extending the list with another list
l2 = [9, 7]
l1.extend(l2)
print(l1)

# Counting the number of occurrences of an element in the list
print("Number of times '8' appears in the list:", l1.count(8))

# Checking if an element is present in the list or not
if 5 in l1:
    print("5 is present in the list")
else:
    print("5 is not present in the list")

# Reversing the list
l1.reverse()
print(l1)

# Slicing the list
print(l1[1:4])  # Output: [9, 6, 2]
print(l1[:4])  # Output: [7, 9, 6, 2]

# Clearing the list
l1.clear()
print(l1)