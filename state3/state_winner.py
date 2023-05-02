from state3 import State


class StateWinner(State):
    def insert_coin(self):
        print("Нельзя вставить монету — нечего продавать")
        from state3 import StateSoldOut
        return StateSoldOut()

    def eject_coin(self):
        print("Монет в приемнике нет, извлечь нечего; жвачки в автомате тоже нет")
        from state3 import StateSoldOut
        return StateSoldOut()

    def turn_crank(self):
        print("Монет в приемнике нет; жвачки в автомате тоже нет")
        from state3 import StateSoldOut
        return StateSoldOut()

    def dispense(self, count: int = 0):
        print("Монет в приемнике нет; жвачки в автомате тоже нет")
        from state3 import StateSoldOut
        return StateSoldOut()