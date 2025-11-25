class Animal:

    def __init__(self, name , breed ):
        self.name = name
        self.breed = breed
    def info(self):
        return f"{self.name}({self.breed})"
        



print(animal1 = Animal("name", "breed"))


