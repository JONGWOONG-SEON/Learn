
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
    