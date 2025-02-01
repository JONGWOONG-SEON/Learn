import sys

class Animal:
    def walk(self):
        pass

class Cat(Animal):
    def walk(self):
        print ("Cat walk")

class Dog(Animal):
    def walk(self):
        print("Dog walk")

def makeWalk(animal:Animal):
    animal.walk()

class Fish:
    def swim(self):
        print("Fish Swim")

class FishAdapter(Animal):
    def __init__(self,fish:Fish):
        self.fish = fish
    
    def walk(self):
        self.fish.swim()

if __name__=="__main__":
    cat = Cat()
    dog = Dog()
    nemo = Fish()
    fish = FishAdapter(nemo)

    makeWalk(cat)
    makeWalk(dog)
    makeWalk(fish)