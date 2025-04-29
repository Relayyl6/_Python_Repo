class Player:
    def __init__(self, name, age, position, shotGoal):
        self.name = name
        self.age = age
        self.position = position
        self.shotGoal = shotGoal
    def defend(self):
        print(self.name, "is defending")

madridPlayer = Player("Cr7", 40, "attack", 11)
madridPlayer.defend()
 