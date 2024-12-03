#"I'm tragically mean like that" - LaRose
#"They're /so/ special" - LaRose
#"Let's make Shelly an actual variable" - LaRose
#"We killed Jerad. Our other animals have to eat something" - Taggart
#"We're not killing anyone" - LaRose
#"There is no knowing" - LaRose
#"Yeah, I remember the pain now" - LaRose
#"You're right. You were crying" - LaRose
#"I can't spell anymore " - LaRose
#"You guys are so difficult" - LaRose
#"Classes are fancy dictionaries" - LaRose
#"Keep them safe and stuff" - LaRose
#"I mean, I can't prove that" - LaRose
#"I used them, so they moved" - LaRose


class Animal:
    def __lt__(self, other):
        return(self.name < other.name)

class Mammal(Animal):
    pass

class Cat(Mammal):
    def __init__(self):
        self.name = "Shelly" 
    def __str__(self):
        return self.name

class Dog(Mammal):
    def __init__(self):
        self.name = "Flash" 
    def __str__(self):
        return self.name

class Robin(Mammal):
    def __init__(self):
        self.name = "Snake" 
    def __str__(self):
        return self.name

class Snake(Mammal):
    def __init__(self):
        self.name = "Robin" 
    def __str__(self):
        return self.name
    
#Cat's methods would resolve first, and then Mammal, and then Animal
#If there's multiple parent classes, it goes through them in order

#Method ResOluition
# print(Cat.mro())
#Directory
# print(dir(Cat))
# print(dir(int))
# print(dir(str))

#The __blank__ fucntions are special and always exist. If you write them, they overwrite the original


shelly = Cat()
# print(shelly.__dict__)
shelly.food = "Lettuce"
# print(shelly.__dict__)

flash = Dog()
robin = Snake()

listed = [shelly, flash, robin]

listed.sort() #This calls __lt__ (less than)

for value in listed:
    print(value)

#self: self is what makes it specific to that object, that specific instance, etc. 
#Each object gets stored at a different location (id is the keyword to see location, i.e. id(shelly))