class student():
    def __init__(self):
        self.__name = " " # __name is private attribute
    
    def getname(self): 
        return self.__name
    def setname(self, n):
        self.__name = n

obj = student()
obj.setname("john")
name = obj.getname()
print(name)

