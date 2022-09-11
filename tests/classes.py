class Dinosaur:
    def __init__(self):
        self.genus = None
        self.gender = None
        self.name = None
        self.size = None


mini_dino = Dinosaur()

mini_dino2 = mini_dino

print(mini_dino)
print(mini_dino2)

mini_dino.size = 10

print(mini_dino.size)
print(mini_dino2.size)
