from .state import State


class StateNoCoin(State):
    def insert_coin(self):
        print("Монета вставлена")
        return State.HAS_COIN

    def eject_coin(self):
        print("Монет в приемнике нет")
        return State.NO_COIN

    def turn_crank(self):
        print("Монет в приемнике нет")
        return State.NO_COIN

    def dispense(self):
        print("Монет в приемнике нет")
        return State.NO_COIN