import sys

class State:
    def handle(self):
        # self.job_state = None
        pass

class ConcreateA(State):
    def __init__(self):
        State.__init__(self)

    def handle(self):
        # print(f"현재 State 는 {self.job_state}")
        print(f"현재 State 는 A")

class ConcreateB(State):
    def __init__(self):
        State.__init__(self)

    def handle(self):
        # print(f"현재 State 는 {self.job_state}")
        print(f"현재 State 는 B")


class Context:
    def __init__(self):
        self._state = State()
    
    def setState(self,state):
        self._state = state

    def request(self):
        self._state.handle()

if __name__ == '__main__':
    stateA = ConcreateA()
    stateB = ConcreateB()

    context = Context()

    context.setState(stateA)
    context.request()

    context.setState(stateB)
    context.request()