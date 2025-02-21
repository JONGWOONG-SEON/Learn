import sys

class SubsystemA:
    def suboperation(self):
        print("Subsystem A method")

class SubsystemB:
    def suboperation(self):
        print("Subsystem B method")

class SubsystemC:
    def suboperation(self):
        print("Subsystem C method")

class Facade:
    def __init__(self):
        self._subA = SubsystemA()
        self._subB = SubsystemB()
        self._subC = SubsystemC()

    def operation(self):
        self._subA.suboperation()
        self._subB.suboperation()
    
    def operation2(self):
        self._subC.suboperation()

if __name__=="__main__":
    facade = Facade()
    facade.operation()
    facade.operation2()