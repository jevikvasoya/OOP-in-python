class emp():
    def __init__ (self, first, last, sal): #constructor self is default
        self.fname = first
        self.lname = last
        self.sal =  sal
        self.email = first + '.' + last + '@gamil.com'

e1 = emp('john', 'wick', '1000')
print(e1.email)
print(e1.sal)
print(e1.fname)













# class pesron():
    
#     def __init__(self, n, o): #constructor
#         print('this is person')
#         self.name = n
#         self.age = o


#     def info(self): 
#         print(self.name) 
#         print(self.age)

# a = pesron("john", '35')
# a.info()  

