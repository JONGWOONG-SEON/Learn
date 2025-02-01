import sys

class Handler:
    def __init__(self):
        self._successor = None
    
    def sethandler(self,successor):
        self._successor = successor

    def handleRequest(self):
        if (self._successor is not None):
            self._successor.handleRequest()

class ConcreateHandler1(Handler):
    def __init__(self):
        Handler.__init__(self)
        self._can_handle = False

    def handleRequest(self):
        if(self._can_handle):
            print("Handled by Concreate Handle 1.")
        else:
            print("Cannot be Handled by Handler 1.") 
            super().handleRequest()

class ConcreateHandler2(Handler):
    def __init__(self):
        Handler.__init__(self)
        self._can_handle = True

    def handleRequest(self):
        if (self._can_handle):
            print("Handled by Create Handler 2.")
        else:
            print("Cannot be Handled by Handler 2.")
            super().handleRequest()

if __name__ == "__main__":
    handler1 = ConcreateHandler1()
    handler2 = ConcreateHandler2()

    handler1.sethandler(handler2)
    handler1.handleRequest()




