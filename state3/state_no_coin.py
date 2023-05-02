from state3.state import State
from typing import Tuple


class StateNoCoin(State):
    def insert_coin(self):
        print("Монета вставлена")
        from state3 import StateHasCoin
        return self

    def eject_coin(self):
        print("Монет в приемнике нет")
        return self

    def turn_crank(self):
        print("Монет в приемнике нет")
        return self

    def dispense(self, count: int = 0) -> Tuple[State, int]:
        print("Монет в приемнике нет")
        return self, count
