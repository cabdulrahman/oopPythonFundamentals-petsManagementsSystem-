#class initialization with deafult__init__
class Pet:
#this is the parent and base class for all pets
    def __init__(self, name, age=None):
        #protected attributes(encapsulation)
        self._name = name
        self.age = age
        #getter and setter methods for encapsulation
    def get_name(self):
        print("Retrieving age")
        return self._name
    def set_age(self, age):
        if type (age) in (int, float) and (age>= 0 and age<=120):
            self.age = age
        else:
            print("Age must be greaterthan 0 or less than 120")
            #encapsulated age property
            age = property(get_name, set_age)
    
    def speak(self):
     # print("sound made")
     return("pet spoke")


class Cat:
    pass
    

class Rat:
    pass

Rasmus = Pet("Scobby", 2)
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

#demonstrating encapsulation
print(f"pet's age :{Rasmus.age}")
Rasmus.age = 5
print(f"pet's age :{Rasmus.age}")