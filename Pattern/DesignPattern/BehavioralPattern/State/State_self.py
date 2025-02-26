from abc import ABC, abstractmethod

class JobState(ABC):
    """Job의 상태를 정의하는 추상 클래스"""
    
    @abstractmethod
    def process(self, job):
        pass

    @abstractmethod
    def complete(self, job):
        pass

    @abstractmethod
    def fail(self, job):
        pass


class PendingState(JobState):
    """작업이 시작되지 않은 상태"""
    def process(self, job):
        print("Job을 실행합니다...")
        job.set_state(RunningState())

    def complete(self, job):
        print("Job이 실행되지 않아 완료할 수 없습니다.")

    def fail(self, job):
        print("Job이 실행되지 않아 실패할 수 없습니다.")


class RunningState(JobState):
    """작업이 실행 중인 상태"""
    def process(self, job):
        print("Job이 이미 실행 중입니다.")

    def complete(self, job):
        print("Job이 성공적으로 완료되었습니다.")
        job.set_state(SuccessState())

    def fail(self, job):
        print("Job이 실패하였습니다.")
        job.set_state(FailedState())


class SuccessState(JobState):
    """작업이 성공적으로 완료된 상태"""
    def process(self, job):
        print("Job이 이미 성공적으로 완료되었습니다.")

    def complete(self, job):
        print("이미 완료된 Job입니다.")

    def fail(self, job):
        print("완료된 Job은 실패할 수 없습니다.")


class FailedState(JobState):
    """작업이 실패한 상태"""
    def process(self, job):
        print("Job이 실패하여 다시 실행할 수 없습니다.")

    def complete(self, job):
        print("실패한 Job을 완료할 수 없습니다.")

    def fail(self, job):
        print("이미 실패한 Job입니다.")


class Job:
    """데이터 파이프라인 Job"""
    def __init__(self):
        self._state = PendingState()  # 초기 상태는 Pending

    def set_state(self, state: JobState):
        self._state = state

    def process(self):
        """Job을 실행하는 메서드"""
        self._state.process(self)

    def complete(self):
        """Job이 완료되었을 때 호출하는 메서드"""
        self._state.complete(self)

    def fail(self):
        """Job이 실패했을 때 호출하는 메서드"""
        self._state.fail(self)


if __name__ == '__main__':
    job = Job()

    job.complete()
    job.fail()
    job.process()
    job.complete()
    job.fail()
