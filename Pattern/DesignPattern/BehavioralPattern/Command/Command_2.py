import sys

class Receiver:
    def action(self):
        print("Receiver: Execute action.")

class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action()

class Invoker:
    def __init__(self):
        self._command = None
    
    def set(self, command):
        self._command = command
    
    def confirm(self):
        if self._command is not None:
            self._command.execute()

if __name__ == "__main__":
    try:
        receiver = Receiver()
        command = ConcreteCommand(receiver)

        invoker = Invoker()
        invoker.set(command)
        
        print("Press Ctrl + C to interrupt...")
        while True:  # 무한 루프 실행
            invoker.confirm()

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt detected! Exiting gracefully.")
        sys.exit(0)

