# Copyright Chai Nunes 2016. MIT Liscence.
import random, os

class Dice:
    def __init__(self, sides=1):
        self.sides = sides
        self.result = []
        self.total = 0

    def _roll(self):
        return random.randint(1, self.sides)

    def roll(self, times=1):
        self.result[:] = [self._roll() for time in range(times)]
        self.sum_result()

    def sum_result(self):
        self.total = sum(self.result)

    def save_result(self, directory=''):
        with open(os.path.join(directory, 'savedResult.txt'), 'a') as txt:
            txt.write('%s\n' % ', '.join(map(str, self.result)))

    def save_total(directory=''):
        with open(os.path.join(directory, 'savedTotal.txt'), 'a') as txt:
            txt.write('%d\n' % self.total)
