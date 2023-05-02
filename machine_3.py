from state3 import State, StateSoldOut, StateNoCoin, StateSold


class GumballMachine():

    def __init__(self):
        self.state: State = StateSoldOut()
        self.count = 0

    def __str__(self):
        return f'Текущее состояние {self.state}; всего жвачек в автомате: {self.count}.'

    def add_gumballs(self, count):
        self.count += count
        print(f'Добавлено жвачек: {count}; всего в автомате: {self.count}')
        if isinstance(self.state, StateSoldOut):
            self.state = StateNoCoin()

    def insert_coin(self):
        self.state = self.state.insert_coin()

    def eject_coin(self):
        print('Извлекаем монету...')
        self.state = self.state.eject_coin()

    def turn_crank(self):
        print('Поворачиваем рычаг...')
        self.state = self.state.turn_crank()
        if isinstance(self.state, StateSold):
            self._dispense()

    def _dispense(self):
        self.state, self.count = self.state.dispense(self.count)


if __name__ == "__main__":
    machine = GumballMachine()
    machine.add_gumballs(3)
    print(machine)

    machine.insert_coin()
    print(machine)
    machine.turn_crank()
    print(machine)

    machine.insert_coin()
    machine.eject_coin()
    machine.turn_crank()
    print(machine)

    #
    machine.insert_coin()
    machine.insert_coin()
    machine.turn_crank()
    print(machine)

    machine.insert_coin()
    machine.turn_crank()
    print(machine)

    machine.insert_coin()
    machine.turn_crank()
    machine.turn_crank()
    machine.turn_crank()
    print(machine)
