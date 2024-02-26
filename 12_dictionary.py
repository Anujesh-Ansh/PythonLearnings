# Dictionary

# A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

# Example:
# Creating a dictionary -> { } or dict()


d1 = {'name': 'Anujesh', 'age': 20, 'city':'Bangalore'}
print(type(d1))                  # Output: <class 'dict'>

# Accessing the value by its key
print('Name : ', d1['name'])     # Output: Anujesh

# You can also access the value using get() method
print('Name : ', d1.get('name')) # Output: Anujesh

# If you try to access a non-existent key, it will throw an error
# print('City : ', d1['country'])  # Output: KeyError: 'country'

# To check if a particular key exists in the dictionary or not, use "in" keyword.
if 'name' in d1:
    print('Name is present in the dictionary')
else:
    print('Name is not present in the dictionary')    


print(d1.values())
print(d1.keys())
print(d1.items())