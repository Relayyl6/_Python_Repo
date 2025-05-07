# class Player:
#     def __init__(self, name, age, position, shotGoal):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.shotGoal = shotGoal
#     def defend(self):
#         print(self.name, "is defending")

# madridPlayer = Player("Cr7", 40, "attack", 11)
# madridPlayer.defend()
 


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return key % self.size
    
    def Insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                print(f"Updated ({key}: {value}) at index {index}")
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)
        print(f"Inserted ({key}: {value}) at index {index}")

# Demo
ht = HashTable()
ht.Insert(5, "apple")  # Inserted (5: apple) at index 5
ht.Insert(15, "orange") # Inserted (15: orange) at index 6 (linear probe)
ht.Insert(5, "banana")  # Updated (5: banana) at index 5
