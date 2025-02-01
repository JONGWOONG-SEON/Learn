# Python Design Pattern : AbstractFactory
# Author:
# 2025

import sys

# 제품에 인터페이스
class ProductA:
    def getName(self):
        pass

# 제품 스펙 구현체
class ConcreateProductAX(ProductA):
    def getName(self):
        return "A-X"

class ConcreateProductAY(ProductA):
    def getName(self):
        return "A-Y"


class ProductB:
    def getName(self):
        pass

class ConcreateProductBX(ProductB):
    def getName(self):
        return "B-X"

class ConcreateProductBY(ProductB):
    def getName(self):
        return "B-Y"


# 팩토리 정의 인터페이스, 생성 책임
class AbstractFactory:
    def createProductA(self):
        pass
    
    def createProductB(self):
        pass

# 팩토리 구현체
class ConcreateFactoryX(AbstractFactory):
    def createProductA(self):
        return ConcreateProductAX()
    
    def createProductB(self):
        return ConcreateProductBX()
    
class ConcreateFacotryY(AbstractFactory):
    def createProductA(self):
        return ConcreateProductAY()
    
    def createProductB(self):
        return ConcreateProductBY()
    

if __name__=='__main__':
    factoryX = ConcreateFactoryX()
    factoryY = ConcreateFacotryY()

    p1 = factoryX.createProductA()
    print ("Product: " + p1.getName())
    
    p2 = factoryY.createProductA()
    print ("Product: " + p2.getName())
    