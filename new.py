# first_dish = (input("Enter your first favorite dish: "))
# second_dish = (input("Enter your second favorite dish: "))
# third_dish = (input("Enter your third favorite dish: "))
# fourth_dish = (input("Enter your fourth favorite dish: "))
# fifth_dish = (input("Enter your fifth favorite dish: "))

# listed_favorite = 'Your favorite dishes are:' + [first_dish, second_dish, third_dish, fourth_dish, fifth_dish]

# listed_favorite = [first_dish, second_dish, third_dish, fourth_dish, fifth_dish]

# for item in listed_favorite:
#     print(item)

# print(listed_favorite[-2])
# print(listed_favorite)

# name = input("what is your name?: ")

# print("Hi " + name)

# is_student = True
# if is_student:
#     print(f"I am a student")



# birth_year = input("Birth year? ")
# age = 2025 - int(birth_year)
# print(type(age))
# print(f"You are {age} years old") 

course = 'Python for Beginners' 
# print(course[0:3]) # from index 0 to index 2, 3 is exclusive 
# print(course[0:]) # from index 0 to the end 
# print(course[:5]) # from index 0 index 4, 5 exclusive
# print(course[:]) # to clone a variable

# let new = String::from("Leonard")
# let first_word = &s[..]

# name = "jennifer"

# first = "Leonard"
# last = "Oseghale"
# # Leonard [Oseghale] is a programmer

# message1 = first + ' [' + last + '] is a programmer'
# message2 =  f'{first} [{last}] is a programmer' 
# print(message1)
# print(message2)

# course = 'Python for Beginners'
# uppercase = course.upper()
# length = len(course)
# print(length, uppercase)
# print('Python' in course)
# x = (2 + 3) * 10 - 3 


# has_good_income = True

# if is_hot:
#     print("It is a sunny day")
# else:
#     print("It is not a sunny day")
# print("Enjoy your day")

# cars=["Volvo", "BMW", "Ford", "Mazda"]
# cars.append("Ferrari")
# cars.pop(1)
# cars.remove("Ford")
# for car in cars:
#     print(f"My {car} is amazing")


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You win")
        break
else: 
    print("Sorry you failed")