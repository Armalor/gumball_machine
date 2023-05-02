from state3.state import State


class StateNoCoin(State):
    def insert_coin(self):
        print("Монета вставлена")
        from state3 import StateHasCoin
        return StateHasCoin()

    def eject_coin(self):
        print("Монет в приемнике нет")
        return StateNoCoin()

    def turn_crank(self):
        print("Монет в приемнике нет")
        return StateNoCoin()

    def dispense(self, count: int = 0):
        print("Монет в приемнике нет")
        return StateNoCoin()