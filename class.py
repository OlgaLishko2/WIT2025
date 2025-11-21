
class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type   

    def check_type(self):
        if self.animal_type.lower() == "mammal":
            return f"{self.name} is a mammal"
        elif self.animal_type.lower() == "amphibian":
            return f"{self.name} is an amphibian"
        elif self.animal_type.lower() == "reptile":
            return f"{self.name} is a reptile"
        else:
            return f"{self.name} is an unknown type"

    def sound(self):
        return "This animal makes a sound"



class Lion(Animal):
    def __init__(self, name="Lion"):
        super().__init__(name, "mammal")


    def check_type(self):
        return f"{self.name} is definitely a mammal — the king of mammals!"


    def sound(self):
        return "ROARRRR!"



a = Animal("Frog", "amphibian")
print(a.check_type())
print(a.sound())

l = Lion()
print(l.check_type())
print(l.sound())
