
# Class and Objects
# class car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def fullname(self):
#         return f"{self.brand} {self.model}"

# obj = car("tata","curv")
# print(obj.brand)
# print(obj.model)
# print(obj.fullname())

# ob = car("kia","carens")
# print(ob.brand)
# print(ob.model)
# print(ob.fullname())


# INHERITENCE

# class car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def fullname(self):
#         return f"{self.brand} {self.model}"

# class electriccar(car):
#     def __init__(self,brand,model,batterysize):
#         super().__init__(brand,model) #access method from car class is called inheritence
#         self.batterysize = batterysize

# obj = car("tata","curv")
# print(obj.brand)
# print(obj.model)
# print(obj.fullname())

# ob = car("kia","carens")
# print(ob.brand)
# print(ob.model)
# print(ob.fullname())

# tesla = electriccar("tesla","T","10KWH")
# print(tesla.fullname())

# POLYMORPHISM
class car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        car.total_car += 1

    def fullname(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):  #polymorphism same method but diffrent work
        return "petrol or diesal"

    @ staticmethod
    def description():
        return "cars are use for transport"

class electriccar(car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model) #access method from car class is called inheritence
        self.batterysize = batterysize
         
    def fuel_type(self): #polymorphism same method but diffrent work
        return "Electric charge"

obj = car("tata","curv")
print(obj.brand)
print(obj.model)
print(obj.fullname())
print(obj.fuel_type())

ob = car("kia","carens")
print(ob.brand)
print(ob.model)
print(ob.fullname())

print(car.total_car)
print(car.description())

# tesla = electriccar("tesla","T","10KWH")
# print(tesla.fullname())
# print(tesla.fuel_type())