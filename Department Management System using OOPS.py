#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#......................MAIN CLASS...................#
class Department:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def speak(self):
        pass 

#....................SUB CLASS-1....................#
class HR(Department):
    def __init__(self, name, hiring):
        super().__init__(name, role="hiring employees")
        self.hiring = hiring
    def speak(self):
        return f"{self.name} says no hirings!"

#...................SUB CLASS-2.....................#    
class Marketing(Department):
    def __init__(self, name, sales):
        super().__init__(name, role="analysing sales")
        self.sales = sales
    def speak(self):
        return f"{self.name} says sale is low!"

#....................SUB CLASS-3.....................#  
class Production(Department):
    def __init__(self, name, income):
        super().__init__(name, role="Calculationg income")
        self.income = income
    def speak(self):
        return f"{self.name} says report is good!"    

#...............INSTANCES FOR SUB CLASSES...............#
hr = HR("Rithika", "vacancy")
mar = Marketing("Praveen", "year end target")
pro = Production("Manoj", "Report")

#...............ACCESS ATTRIBUTES & PRINT...............#
print(f"{hr.name} is a {hr.role} if there is {hr.hiring}.", end=" ")
print(hr.speak())
print(f"{mar.name} is a {mar.role} for {mar.sales}.", end=" ")
print(mar.speak())
print(f"{pro.name} is a {pro.role} for {pro.income}. ", end=" ")
print(pro.speak())

