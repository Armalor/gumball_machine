class GumballMachine():
    SOLD_OUT = 0
    NO_COIN = 1
    HAS_COIN = 2
    SOLD = 3

    def __init__(self):
        self.state = GumballMachine.SOLD_OUT
        self.count = 0

    def __str__(self):
        states = {
            GumballMachine.SOLD_OUT: 'SOLD_OUT',
            GumballMachine.NO_COIN: 'NO_COIN',
            GumballMachine.HAS_COIN: 'HAS_COIN',
            GumballMachine.SOLD: 'SOLD',
        }
        return f'Текущее состояние {self.state} ({states[self.state]}); всего жвачек в автомате: {self.count}.'

    def add_gumballs(self, count):
        self.count += count
        print(f'Добавлено жвачек: {count}; всего в автомате: {self.count}')
        if self.state == GumballMachine.SOLD_OUT:
            self.state = GumballMachine.NO_COIN

    def insert_coin(self):
        if self.state == GumballMachine.HAS_COIN:
            print("Нельзя вставлять несколько монет")
        elif self.state == GumballMachine.NO_COIN:
            self.state = GumballMachine.HAS_COIN
            print("Монета вставлена")
        elif self.state == GumballMachine.SOLD_OUT:
            print("Нельзя вставить монету — нечего продавать")
        elif self.state == GumballMachine.SOLD:
            print("Пожалуйста, подождите пока будет выдана жувачка!")

    def eject_coin(self):
        if self.state == GumballMachine.HAS_COIN:
            print("Монета возвращена")
            self.state = GumballMachine.NO_COIN
        elif self.state == GumballMachine.NO_COIN:
            print("Монет в приемнике нет")
        elif self.state == GumballMachine.SOLD_OUT:
            print("Монет в приемнике нет")
        elif self.state == GumballMachine.SOLD:
            print("Сорян, но жвачка уже продана вам, наслаждайтесь")

    def turn_crank(self):
        if self.state == GumballMachine.HAS_COIN:
            print('Выдаем жувачку!')
            self.state = GumballMachine.SOLD
            self._dispense()
        elif self.state == GumballMachine.NO_COIN:
            print('Нет монетки в приемнике')
        elif self.state == GumballMachine.SOLD_OUT:
            print('Нечего продать, автомат пуст')
        elif self.state == GumballMachine.SOLD:
            print("Уже выдаем жвачку, не дергайте лишний раз, просто подождите, пожалуйста")

    def _dispense(self):
        if self.state == GumballMachine.HAS_COIN:
            print('Сначала нужно нажать на рычаг')
        elif self.state == GumballMachine.NO_COIN:
            print('Сначала нужно оплатить покупку')
        elif self.state == GumballMachine.SOLD_OUT:
            print('Нечего продать, автомат пуст')
        elif self.state == GumballMachine.SOLD:
            print('Жвачка выдана!')
            self.count -= 1
            if self.count > 0:
                self.state = GumballMachine.NO_COIN
            else:
                self.state = GumballMachine.SOLD_OUT


if __name__ == "__main__":
    machine = GumballMachine()
    machine.add_gumballs(3)

    machine.insert_coin()
    machine.turn_crank()

    print(machine)

    machine.insert_coin()
    machine.eject_coin()
    machine.turn_crank()
    print(machine)

    machine.insert_coin()
    machine.insert_coin()
    machine.turn_crank()
    print(machine)
