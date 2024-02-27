# Packages
# A package is a collection of modules. It must contain an __init__.py file as a flag to Python that it is a package.

# Example:

# pip install camelcase
import camelcase as cs

c = cs.CamelCase() # Creating an object of the class CamelCase from camelcase module

txt = "hello world"

print(c.hump(txt))   # Converting to hump case i.e. Hello World

# Output: helloWorld

#This method capitalizes the first letter of each word.
