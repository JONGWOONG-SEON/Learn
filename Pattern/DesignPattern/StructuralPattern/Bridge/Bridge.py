import sys

class Implementor:
  def action(self):
    pass


class ConcreteImplementorA(Implementor):
  def action(self):
    print("Create by ConcreateImplemntorA")

class ConcreateImplementorB(Implementor):
  def action(self):
    print("Create by ConcreateImplemntorA")

class Bridge:
  def __init__(self,implementor):
    self._implementor = implementor

  def operation(self):
    self._implementor.action()

if __name__=='__main__':
  ConcreateA = Bridge(ConcreteImplementorA())
  ConcreateA.operation()

  ConcreateB = Bridge(ConcreateImplementorB())
  ConcreateB.operation()