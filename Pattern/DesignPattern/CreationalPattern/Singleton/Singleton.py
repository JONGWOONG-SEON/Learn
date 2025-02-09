import sys

class SingletonDeco:
    def __init__(self,instance):
        self._instance = instance

    def __call__(self):
        raise TypeError("...")
    
    def get(self):
        try:
            return self._only
        except AttributeError:
            self._only = self._instance()
            return self._only

@SingletonDeco
class Class:
    def tell(self):
        print("This is Singleton.")

if __name__ == "__main__":
    singleton = Class.get()
    singleton.tell()