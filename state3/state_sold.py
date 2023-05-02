from state3.state import State


class StateSold(State):
    def insert_coin(self):
        print("Пожалуйста, подождите пока будет выдана жувачка!")
        return StateSold()

    def eject_coin(self):
        print("Сорян, но жвачка уже продана вам, не можем вернуть монету")
        return StateSold()

    def turn_crank(self):
        print("Уже выдаем жвачку! Не дергайте лишний раз, просто подождите, пожалуйста")
        return StateSold()

    def dispense(self, count: int = 0):
        print(f'Идет процесс выдачи... Завершен! {count}')
        count -= 1
        from state3 import StateNoCoin, StateSoldOut
        return StateNoCoin() if count else StateSoldOut(), count
