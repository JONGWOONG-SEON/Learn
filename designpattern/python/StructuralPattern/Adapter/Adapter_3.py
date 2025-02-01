
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
