class Dog:
    def __init__(self, name, breed, owner):
        self.name = name   # this shows the dog has a name attribute
        self.breed = breed # this shows the dog has a breed attribute
        self.owner = owner # this shows the dog has a owner attribute

    def bark(self):        # Methods are functions defined insde of a class
        print("woof woof")

class Owner:
    def __init__(self, name , address , contact_number):
        self.name = name
        self.address = address 
        self.phone_number = contact_number
        
owner1 = Owner("Daniel", "24th Boulevard", "011-583-92")
dog1 = Dog("Bruce", "German Sherpard", owner1)
# dog1.bark()
# print(dog1.name)
# print(dog1.breed)
print(dog1.owner.name)

owner2 = Owner("Leroy", "12th Avenue", "011-584-65")
dog2 = Dog("Ferdinand", "Scottish Bulldog", owner2)
# dog2.bark()
# print(dog2.name)
# print(dog2.breed)
print(dog2.owner.name)


