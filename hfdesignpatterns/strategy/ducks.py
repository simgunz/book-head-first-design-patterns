import abc

from .behaviours.fly import FlyWithWings
from .behaviours.quack import Quack


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


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behaviour = Quack()
        self.fly_behaviour = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")
