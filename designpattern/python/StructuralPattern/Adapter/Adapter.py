#
# Python design pattern : Adapter
# Author :
# 2025
#

'''
import sys

class Adaptee:
    def specificRequest(self):
        print("Specifiy Request")

class Target:
    def request(self):
        pass

class Adapter(Target,Adaptee):
    def __init__(self):
        Target.__init__(self)
        Adaptee.__init__(self)

    def request(self):
        return self.specificRequest()

if __name__ == '__main__':
    t = Adapter()
    t.request()
'''

'''
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
'''

'''
import sys

class Target:
    def request(self):
        pass

def makeAction(target : Target):
    target.request()
    
class Adaptee:
    def newRequest(self):
        print("New Specify Request")

class Adpater(Target,Adaptee):
    def __init__(self):
        Target.__init__(self)
        Adaptee.__init__(self)

    def request(self):
        return self.newRequest()
    
if __name__ == '__main__':
    p1 = Adpater()
    
    makeAction(p1)
'''


import sys

class Animial:
    def walk(self):
        print("Animal Walk")

def makeWalk(animal:Animial):
    animal.walk()

class Fish:
    def swim(self):
        print("Fish Swimming")

class WalkAdapter(Animial,Fish):
    def __init__(self):
        Animial.__init__(self)
        Fish.__init__(self)
    
    def walk(self):
        return self.swim()

if __name__ == "__main__":
    
    p1 = WalkAdapter()
    makeWalk(p1)
    