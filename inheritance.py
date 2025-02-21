#single inheritance

# class A():
#     def displayA(self):
#         print("welcome A")

# class B(A):  # all properties of A in B
#     def displayB(self):
#         print("welcome B")
    
# obj = B()
# obj.displayA()
# obj.displayB()



#muliple inheritance

# class A():
#     def displayA(self):
#         print("welcome A")

# class B():  # all properties of A in B
#     def displayB(self):
#         print("welcome B")

# class C(A,B): # all properties of A and B in C
#     def displayC(self):
#         print("welcome C")
    
# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()


#multilevel inheritance

class animal():
    def eat(self):
        print("eating...")

class dog(animal):
    def bark(self):
        print("barking...")

class cat(dog):
    def meow(slef):
        print("meowing...")

obj = cat()
obj.eat()
obj.bark()
obj.meow()