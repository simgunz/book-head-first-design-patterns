import abc


class Subject(abc.ABC):
    def __init__(self):
        self.observers = set()

    def register_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    @abc.abstractmethod
    def notify_observers(self):
        pass


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self):
        raise NotImplementedError()
