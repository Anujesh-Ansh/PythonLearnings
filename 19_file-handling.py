# File Handling
# File handling is an important part of any web application. In this section, we will discuss how to handle files in Python.

# Writing a File
s = "Hi Anujesh"
fp = open("file.txt", "w")
fp.write(s)
fp.close()

# with open("file.txt", "w") as fp:
#     fp.write(s)

# Reading a File
fp = open("file.txt", "r")
print(fp.read())  # Prints the entire content of file