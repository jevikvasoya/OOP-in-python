# import math
# class circle():
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2

# o = circle(42)
# o1 = circle(7)
# print(o.area())
# print(o1.area())

class Bank:
    def __init__(self):
        self.user_data = {}  

    def add_user(self, user_id):
        if user_id not in self.user_data: #check already user_id wxist
            self.user_data[user_id] = 0 

    def deposit(self, user_id, amount):
        if user_id in self.user_data and amount > 0:
            self.user_data[user_id] += amount
            print("deposite")
        else:
            print("Invalid deposit")

    def withdrawal(self, user_id, amount):
        if user_id in self.user_data and self.user_data[user_id] >= amount:
            self.user_data[user_id] -= amount
            print("withdrwal")
        else:
            print("invalid balance")

    def current_balance(self, user_id):
        if user_id in self.user_data:
            return self.user_data[user_id]
        else:
            return "invalid"


bank_obj = Bank()


bank_obj.add_user("user1")
bank_obj.add_user("user2")

bank_obj.deposit("user1", 500)
bank_obj.withdrawal("user1", 300)

bank_obj.deposit("user2", 1500)
bank_obj.withdrawal("user2", 500)

balances = {
    "user1": bank_obj.current_balance("user1"),
    "user2": bank_obj.current_balance("user2")
}                                        
print(balances)





