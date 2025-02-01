import sys

class Work:
    def __init__(self):
        self._worker = None

    def setWorker(self,worker):
        self._worker = worker
    
    def WorkerRequest(self):
        if (self._worker is not None):
            self._worker.WorkerRequest()

class AssignWorker1(Work):
    def __init__(self):
        Work.__init__(self)
        self._can_work = False
        
    def WorkerRequest(self):
        if (self._can_work):
           print("Do worker 1")
        else:
            print("Cant Work 1")
            super().WorkerRequest()

class AssignWorker2(Work):
    def __init__(self):
        Work.__init__(self)
        self._can_work = True 

    def WorkerRequest(self):
        if (self._can_work):
            print("Do worker 2")
        else:
            print("Cant Work 2")
            super().WorkerRequest()

if __name__ == "__main__":
    
    worker1 = AssignWorker1()
    worker2 = AssignWorker2()
    
    worker1.setWorker(worker2)
    worker1.WorkerRequest()