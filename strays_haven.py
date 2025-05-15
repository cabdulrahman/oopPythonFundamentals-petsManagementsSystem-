#class initialization with deafult__init__
class Pet:
      
    def speak(self):
      print("sound made")
Rasmus = Pet()
Rasmus.name = "Rasmus"
print(Rasmus.name)
print(Rasmus.speak())
class Dog:

    species = "Canis  lupus familiaris"# class attribute
    
    def __init__(self, name,breed,age = "N/A"):
        self.name = name# instance attribute
        self.breed = breed
        self.age = age
    def speak(self):
       return f"{self.name} says woof! woof!"
koba = Dog("Koba", "Great Done", 3)
amad= Dog("Amad", "Black Goat")
koba.age = 4
print(koba.speak())
print(koba.age)
print(amad.age)

class Cat:
    pass
    

class Rat:
    pass

