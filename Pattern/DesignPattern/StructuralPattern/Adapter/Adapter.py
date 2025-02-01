#
# Python design pattern : Adapter
# Author :
# 2025
#


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


