# class parrot():
#     def fly(self):
#         print("parrot can fly")

#     def swim(self):
#         print("parrot can't swim")

# class penguin():
#     def fly(self):
#         print("penguin can't fly")

#     def swim(self):
#         print("penguin can swim")

# def fly_test(bird): 
#     bird.fly()

# pa = parrot()
# pe = penguin()

# fly_test(pa)
# fly_test(pe)




#method overloading (same function name with different parameters)
# class area():
#     def find_area(self, x=None, y=None):

#         if x != None and y != None:
#             print(x*y)
#         elif x!= None:
#             print(x*x)
#         else:
#             print("nothing")

# obj = area()
# obj.find_area()
# obj.find_area(10)
# obj.find_area(10,20)


#method overriding (same function name with same parameters)
class A():
    def show(self):
        print("class A")

class B(A):
    def show(self):
        print("class B")
obj = B()
obj.show()