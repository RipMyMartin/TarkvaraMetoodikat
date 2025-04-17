class Player:
    def init__(self, hp, energy, food):
        self.hp = hp
        self.energy = energy
        self.food = food

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 3
            print("You rested and gained (3 energy)!!!")
        else:
            print("You don't have enough food to rest!!!")

