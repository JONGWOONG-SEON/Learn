import sys

class Recevier:
    def action(self):
        print("Receiver : excute action.")

class Command:
    def excute(self):
        pass

class ConcreateCommand(Command):
    def __init__(self,recevier):
        self._recevier = recevier

    def excute(self):
        self._recevier.action()

class Invoker:
    def __init__(self):
        self._command = None
    
    def set(self,command):
        self._command = command
    
    def confirm(self):
        if (self._command is not None):
            self._command.excute()

if __name__ == "__main__":
    recevier = Recevier()
    command = ConcreateCommand(recevier)

    invoker = Invoker()
    invoker.set(command)
    invoker.confirm()