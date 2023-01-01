from .state import State


class StateSold(State):
    def insert_coin(self):
        print("Пожалуйста, подождите пока будет выдана жувачка!")
        return State.SOLD

    def eject_coin(self):
        print("Сорян, но жвачка уже продана вам, не можем вернуть монету")
        return State.SOLD

    def turn_crank(self):
        print("Уже выдаем жвачку! Не дергайте лишний раз, просто подождите, пожалуйста")
        return State.SOLD

    def dispense(self):
        print('Идет процесс выдачи... Завершен!')
        return State.NO_COIN
