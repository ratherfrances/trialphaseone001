# # class Card: 
# #   def __init__(self,v,s): 
# #       self.value = v
# #       self.suit = s

# #   def __repr__(self):
# #       return "Hello"

# # c1 = Card(7,"diamonds")
# # print(c1.value)
# # print(c1.suit)




# # F STRING - UNRELATED TO CLASS 
# # #f-strings
# # name = "Laszlo"
# # fav_food = "pancakes"
# # print(f"Hi, I'm {name}.  I like {fav_food}.") 



# # class Card:
# #     def __init__(self,v,s):
# #         self.value = v
# #         self.suit = s
# #     def __repr__(self):
# #         return f"{self.value}{self.suit[0]}"
# # c1 = Card(9,"spades")
# # print(c1)  
# # print(c1.value)
# # print(c1.suit) 
































# # class Customer:
# #     def __init__(self,name,balance):
# #         self.name = name
# #         self.balance = balance
# #     def deposit(self,amount):
# #         self.balance = self.balance + amount
# #     def get_o_count(self):
# #         total = 0
# #         for char in self.name:
# #             if char == "o":
# #                 total += 1
# #         return total
# # customer1 = Customer("John Doe",1000.23)
# # x = customer1.get_o_count()
# # print(x) 




# class User:
#     def __init__(self,username,bio):
#         self.username = username
#         self.bio = bio 
#         self.points = points 

#     def change_username(self,new_username): 


# user1 = User("Joyce Lynn","no descriprion yet", 0)
# print(user1.username) 


# user1.change_username("PoodleTalk123")

# print(user1.username)




# class Card:
#     def __init__(self,v,s):
#         self.value = v
#         self.suit = s
#         self.color = self._determine_color()
#     def _determine_color(self):
#         if self.suit in ["diamonds","hearts"]:
#             return "red"
#         elif self.suit in ["clubs","spades"]:
#             return "black"
# c1 = Card(7,"diamonds")
# print(c1.value)
# print(c1.suit) 
# print(c1.color) 



cc_number = ()

for i in range(cc_number):
    if i == 16:
        print('Visa, Master Card, Discover')
    elif i == 15:
        print('Amex')
    # else:
    #     print('invalid number')












