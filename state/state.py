from abc import ABC, abstractmethod

class State(ABC):
    SOLD_OUT = 0
    NO_COIN = 1
    HAS_COIN = 2
    SOLD = 3

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
    def dispense(self):
        pass
