# # User Input
# The input() function allows for user input. The input function takes a single argument, which is the prompt string. 
# The prompt string is displayed to the user, and the user's input is returned as a string.

# Example:
name = input("Enter your name: ")
print(f"Hello {name}!")
# Output:
# Enter your name: Anujesh
# Hello Anujesh!

# The input function always returns a string. 
# If you want to convert the input to a different type, you can use the appropriate type casting function.

# Example:
age = int(input("Enter your age: "))  # Convert user input to integer
if age < 0:
    print("Age cannot be negative")
elif age == 0:
    print("You are a baby")
else:
    print(f"You are {age} years old")


