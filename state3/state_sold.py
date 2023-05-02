from state3.state import State
from typing import Tuple


class StateSold(State):
    def insert_coin(self):
        print("Пожалуйста, подождите пока будет выдана жувачка!")
        return self

    def eject_coin(self):
        print("Сорян, но жвачка уже продана вам, не можем вернуть монету")
        return self

    def turn_crank(self):
        print("Уже выдаем жвачку! Не дергайте лишний раз, просто подождите, пожалуйста")
        return self

    def dispense(self, count: int = 0) -> Tuple[State, int]:
        print(f'Идет процесс выдачи {count} → {count - 1}... Завершен!')
        count -= 1
        from state3 import StateNoCoin, StateSoldOut
        return StateNoCoin() if count else StateSoldOut(), count
