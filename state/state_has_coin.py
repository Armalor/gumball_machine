from .state import State

class StateHasCoin(State):
    def insert_coin(self):
        print("Нельзя вставлять несколько монет")
        return State.HAS_COIN

    def eject_coin(self):
        print("Монета возвращена")
        return State.NO_COIN

    def turn_crank(self):
        print('Выдаем жувачку!')
        return State.SOLD

    def dispense(self):
        print('Пока рано, готовим процесс выдачи')
        return State.HAS_COIN
