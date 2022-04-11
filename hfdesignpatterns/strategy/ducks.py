import abc


class Duck(abc.ABC):
    def __init__(self):
        self.quack_behaviour = None
        self.fly_behaviour = None

    @abc.abstractmethod
    def display(self):
        raise NotImplementedError

    def perform_fly(self):
        self.fly_behaviour.fly()

    def perform_quack(self):
        self.quack_behaviour.quack()

    def swim(self):
        print("All ducks float, even decoys!")
