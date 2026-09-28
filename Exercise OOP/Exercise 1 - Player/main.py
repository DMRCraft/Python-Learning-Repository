# Basic Player Class

class Player:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def level_up(self):
        self.level + 1

    def __str__(self):
        return f"'{self.name}', HEALTH: {self.health}, LEVEL: {self.level}"

player1 = Player("DMR", 100, 25)
player2 = Player("John123", 75, 0)
player3 = Player("xX_Bob_Xx", 20, 100)

player1.take_damage(20)
player2.heal(25)
player3.level_up()

print(player1)
print(player2)
print(player3)