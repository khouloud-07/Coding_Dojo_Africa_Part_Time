class User:
    #! constructor
    def __innit__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
#! Object
def display_info(self):
    print(f"First name: {self.first_name}")
    print(f"Last name: {self.last_name}")
    print(f"Email: {self.email}")
    print(f"Age: {self.age}")
    print(f"Member: {self.is_rewards_member}")
    print(f"Current Points: {self.gold_card_points}")

def enroll(self):
    self.gold_card_points = 20
    if (self.is_rewards_member == True):
        print("User already a member.")
        return False
    else :
        return True

def spend_points(self, amount):
    if self.gold_card_points < amount:
            print("Insufficient points.")
            return False
    self.gold_card_points -= amount



user_7 = User("Khouloud", "Farhati", "khouloudfarhati@gmail.com", 20)
user_1 = User("Nermine", "Farhati", "monifarhati@gmail.com", 20)
user_2 = User("Moni", "Farhati", "nerminefarhati@gmail.com", 20)
user_7.display_info()
user_7.enroll()
user_1.spend_points(50).enroll()
user_2.enroll().spend_points(80)
user_1.display_info()
user_2.display_info()