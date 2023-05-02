from state3.state import State


class StateHasCoin(State):
    def insert_coin(self):
        print("Нельзя вставлять несколько монет")
        return StateHasCoin()

    def eject_coin(self):
        print("Монета возвращена")
        # Не можем вынести import наверх, т.к. получим ошибку циклического импорта:
        # https://tonais.ru/osnovy/tsiklicheskiy-import-v-python
        from state3 import StateNoCoin
        return StateNoCoin()

    def turn_crank(self):
        print('Выдаем жувачку!')
        from state3 import StateSold
        return StateSold()

    def dispense(self, count: int = 0):
        print('Пока рано, готовим процесс выдачи')
        return StateHasCoin()
