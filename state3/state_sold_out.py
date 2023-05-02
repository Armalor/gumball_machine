from state3.state import State
from typing import Tuple


class StateSoldOut(State):
    def insert_coin(self):
        print("Нельзя вставить монету — нечего продавать")
        return self

    def eject_coin(self):
        print("Монет в приемнике нет, извлечь нечего; жвачки в автомате тоже нет")
        return self

    def turn_crank(self):
        print("Монет в приемнике нет; жвачки в автомате тоже нет")
        return self

    def dispense(self, count: int = 0) -> Tuple[State, int]:
        print("Монет в приемнике нет; жвачки в автомате тоже нет")
        return self, count