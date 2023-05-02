from abc import ABC, abstractmethod


class State(ABC):

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def eject_coin(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self, count: int = 0):
        pass
