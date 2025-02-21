# class democlass(): # class definition
#     a = 10
 
# demoobject = democlass() # object creation
# demoobject1 = democlass()

# print(demoobject.a) # accessing class variable using object
# print(demoobject1.a) 



# class democlass():
#     a = 10

#     def sum(self): # method definition
#         print(20+30)

# demoobject = democlass()
# demoobject.sum()

# class person():
#     name = 'john'
#     age = 23

# x = person()
# print(x.name)

# x.age = 30
# print(x.age)


"""
class 

bank system 

deposit 
condition money grater than 0 

withdrawl amuont 
check current balance if valid then withdraw money 

make one another method check current balance
return current balance 
"""

class bank():
    def __init__(self):
        self.balance = 0
    
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print("deposite",amount) 
        else:
            print("invalid")
    
    def withdrwal(self,amount):
        if self.balance >= amount:
           self.balance -= amount
           print("withdrwal")
        else:
            print("not withdrwal")
            
    def current(self):
        print(self.balance)
    
    
    
obj = bank()
obj.deposite(1000)
obj.withdrwal(500)
obj.current()

obj.deposite(1500)
obj.withdrwal(300)
obj.current()



