# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# person1 = Person("Alice", 39)
# person1.greet()

# person2 = Person("john", 25)
# person2.greet()


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email 
        self.password = email 

    def say_hi_to_user(self, user):
        print(f"sending message to {user.username}: Hi {user.username}, it's {self.username}")


user1 = User("Leonard", "oseghaleleonard39@gmail.com", "12345678")
user2 = User("Daniel", "Danielakpata12@gmail.com", "password")

user1.say_hi_to_user(user2)
user1.email = "Leonard@gmail.com"
print(user1.email)

