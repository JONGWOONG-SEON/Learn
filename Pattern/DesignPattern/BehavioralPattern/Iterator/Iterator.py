import sys

class Aggreate:
    def __init__(self):
        self._list=[]
    
    def __iter__(self):
        return Iterator(self._list)
    
    def get(self,index):
        return self._list[index]
    
    def set(self,l):
        self._list = l

class Iterator:
    def __init__(self, aggreate):
        self._list = aggreate
        self._size = len(aggreate)
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if  self._index < self._size:
            pos = self._index
            self._index += 1
            return aggreate.get(pos)

        else:
            raise StopIteration()
        
if __name__ == '__main__':
    aggreate = Aggreate()
    aggreate.set([10,20,30,40,50])

    for value in list(aggreate):
        print("Item value : " + str(value))