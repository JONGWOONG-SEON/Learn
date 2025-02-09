class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # 최초 인스턴스가 생성될 때만 인스턴스를 할당
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        else:
            # 두 번째 이후의 인스턴스 생성 시 오류 발생
            raise TypeError("Singleton class cannot have more than one instance.")
        return cls._instance

    def __init__(self):
        # 초기화 코드 (최초 한 번만 호출)
        if not hasattr(self, 'initialized'):  # 이미 초기화 되었는지 확인
            self.initialized = True
            print("Singleton instance created.")

    def tell(self):
        print("This is the Singleton instance.")

if __name__ == "__main__":
    singleton1 = Singleton()  # 첫 번째 인스턴스
    singleton1.tell()

    singleton2 = Singleton()  # 두 번째 인스턴스를 생성하려고 시도
    singleton2.tell()