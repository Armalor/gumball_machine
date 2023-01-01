from .state import State


class StateSoldOut(State):
    def insert_coin(self):
        print("Нельзя вставить монету — нечего продавать")
        return State.SOLD_OUT

    def eject_coin(self):
        print("Монет в приемнике нет, извлечь нечего; жвачки в автомате тоже нет")
        return State.SOLD_OUT

    def turn_crank(self):
        print("Монет в приемнике нет; жвачки в автомате тоже нет")
        return State.SOLD_OUT

    def dispense(self):
        print("Монет в приемнике нет; жвачки в автомате тоже нет")
        return State.SOLD_OUT