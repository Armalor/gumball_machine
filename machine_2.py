from state import State, StateSoldOut, StateSold, StateNoCoin, StateHasCoin


class GumballMachine():

    def __init__(self):
        self.state: int = State.SOLD_OUT
        self.count = 0

        self.__states = {
            State.SOLD_OUT: StateSoldOut(),
            State.NO_COIN: StateNoCoin(),
            State.HAS_COIN: StateHasCoin(),
            State.SOLD: StateSold(),
        }

    def __str__(self):
        states = {
            State.SOLD_OUT: 'SOLD_OUT',
            State.NO_COIN: 'NO_COIN',
            State.HAS_COIN: 'HAS_COIN',
            State.SOLD: 'SOLD',
        }

        return f'Текущее состояние {self.state} ({states[self.state]}); всего жвачек в автомате: {self.count}.'

    def add_gumballs(self, count):
        self.count += count
        print(f'Добавлено жвачек: {count}; всего в автомате: {self.count}')
        if self.state == State.SOLD_OUT:
            self.state = State.NO_COIN

    def insert_coin(self):
        self.state = self.__states[self.state].insert_coin()

    def eject_coin(self):
        print('Извлекаем монету...')
        self.state = self.__states[self.state].eject_coin()

    def turn_crank(self):
        print('Поворачиваем рычаг...')
        self.state = self.__states[self.state].turn_crank()
        if State.SOLD == self.state:
            self._dispense()

    def _dispense(self):
        self.state = self.__states[self.state].dispense()
        self.count -= 1


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
    # machine.insert_coin()
    # machine.insert_coin()
    # machine.turn_crank()
    # print(machine)
