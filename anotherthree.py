class Player:
    name = ""
    age = 0
    position = ""
    shotGoal = 0
    def defend(self):
        print(self.name, "is defending")

madridPlayer = Player()
madridPlayer.name = "Cr7"
madridPlayer.age = 40
madridPlayer.position = "Striker"
madridPlayer.shotGoal = 2
madridPlayer.defend()
