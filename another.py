class Player():
    def __init__(self, name, age, position, shotGoal):
        self.name = name
        self.age = age
        self.position = position
        self.shotGoal = shotGoal
    
    def defend(self):
        print(self.name, "is defending")
    
madridPlayer = Player("CR7", 40, "attack", 11)
madridPlayer.defend()


class Player: 
    name = ""
    age = 0
    position = ""
    shotGoal = 0

    def defend(self):
        print(self.name, "is defending")

madridPlayer = Player()
madridPlayer.name = "CR7"
madridPlayer.age = 40
madridPlayer.position = "Striker"
madridPlayer.defend()
