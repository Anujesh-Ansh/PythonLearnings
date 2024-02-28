# OOPS -> Object Oriented Programming System
# Class - Blueprint for creating objects of a specific class. 
# Objects are instances of classes, and they can have attributes and methods.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary, self.name
    

rohan = Employee('Rohan', 455)
print(rohan.salary)
print(rohan.name)


ansh = Employee('Ansh', 45500)
print(ansh.salary)
print(ansh.name)
