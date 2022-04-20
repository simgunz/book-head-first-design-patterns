import abc


class DisplayElement(abc.ABC):
    @abc.abstractmethod
    def display(self):
        raise NotImplementedError()
