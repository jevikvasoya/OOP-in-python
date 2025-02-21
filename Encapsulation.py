# Encapsulation is private attribute and methods.

class student():

    __name = "harry" # __name is private variable
    def __init__(self):
        print(self.__name) 
        self.__show() # private method

    def __show(self):
        
        print("welcome")

obj = student()

# print(obj.__name) # not accessible because it is private variable
