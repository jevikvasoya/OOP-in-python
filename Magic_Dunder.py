# class emp():
#     name = "harry"
#     def __len__(self): # dunder method
#         i = 0
#         for c in self.name:
#             i = i+1
#         return i

# e = emp()
# print(e.name)
# print(len(e))


# operator overloading
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# overriding magic method
    def __add__(self,other):
        return self.x + other.x, self.y + other.y

p1 = point(10, 20)
p2 = point(30, 40)

print(p1+p2)