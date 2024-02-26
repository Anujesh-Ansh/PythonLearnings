# While Loop
# This is a simple while loop that iterates over a list of numbers and prints each number. The loop continues until the condition is true, as soon as it becomes false, at that point the loop stops.

# Syntax:
# while condition:
    # code to execute (usually an indented block)

# The "while" loop will continue to run as long as the condition is true. If the condition is false, the loop will stop.
# The "while" loop is used when the number of iterations is not known in advance. 
# It continues executing a block of code as long as the condition is true. Once the condition becomes false, it stops executing the block of code.

i = 0
while(i<10):
    print(i)
    i = i + 1
    
print("Loop completed")


# Infinite While Loop (When Condition is always true):
while(True):
    x = int(input('Enter a number: '))
    if x == 0:
        print("You entered 0. Exiting the loop.")
        break
    if x == 3:
        print("You entered 3. Skipping the loop.")
        continue
    print("You entered: ", x)

print("Loop completed")

# The "break" statement is used to exit the loop. It is used to terminate the loop prematurely.
