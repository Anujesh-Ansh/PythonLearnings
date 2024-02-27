# Strings

# Strings are used in Python to record text information, such as name. 
# Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. 

# For example, 
# Python understands the string "hello" to be a sequence of letters in a specific order. 
# This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).


# Creating a string
a = 'Anujesh'
print(a)

# # String Methods
# Accessing elements of a string using indexing:
print(a[0])   # Output: A
print(a[-1])  # Output: h
print(a[2:5]) # Output: uje

# String Concatenation
b = a + ' Ansh'
print(b)     # Output: Anujesh Ansh

# UpperCase
print(a.upper())  # Output: ANUJESH

# LowerCase
print(a.lower())  # Output: anujesh

# Finding length of a string
print(len(a))     # Output: 7

# Checking if a substring is present in a string
print('j' in a)    # Output: True
print('k' not in a) # Output: True

# String Formatting
name = 'Anujesh'
age = 34
country = 'India'

formatted_string = f"My name is {name}, I am {age} years old, and I am from {country}."
print(formatted_string)  # Output: My name is Anujesh, I am 34 years old, and I am from India.

# Strip leading/trailing spaces
spacey_string = '      Hello World!     '
cleaned_string = spacey_string.strip()
print(cleaned_string)       # Output: Hello World!

# Split a string into list of substrings based on a delimiter
sentence = "I love coding in Python"
words = sentence.split(" ")
print(words)              # Output: ['I', 'love', 'coding', 'in', 'Python']

# Joining list of strings to form a single string with a delimiter
word_list = ["Hello", ",", "World", "!"]
joined_string = "".join(word_list)
print(joined_string)        # Output: Hello,World!  (No space between words)

# Replace a substring with another substring
original_string = "The quick brown fox jumps over the lazy dog"
new_string = original_string.replace("fox", "cat")
print(new_string)            # Output: The quick brown cat jumps over the lazy dog

# Count the number of occurrences of a substring in a string
string = "Python is awesome, I love Python"
substring = "Python"
count = string.count(substring)
print(count)                # Output: 2

# Get character at specific index
character = string[0]
print(character)             # Output: P

# Slice a string - get part of the string
part_of_string = string[5:10]   # Output: love Python

# Check if a substring is present in a string
is_present = "Python" in string
print(is_present)               # Output: True
