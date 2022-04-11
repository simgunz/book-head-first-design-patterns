import abc


class FlyBehavior(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        raise NotImplementedError()


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRockets(FlyBehavior):
    def fly(self):
        print("I'm flying with rockets")
