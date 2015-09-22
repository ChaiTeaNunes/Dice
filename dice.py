# Copyright Chai Nunes 2015. MIT Liscence.
import random, os

class Dice:
    result = []
    total = 0

    def __roll_(sides=1):
        return random.randint(1, sides)

    def roll(sides=1, times=1):
        for time in range(0, times):
            Dice.result.append(Dice.__roll_(sides))
            Dice.result = Dice.result[len(Dice.result) - times:len(Dice.result)]
        Dice.sumResult()
        return Dice.result

    def sumResult():
        Dice.total = 0
        for num in range(0, len(Dice.result)):
            Dice.total += Dice.result[num]
        return Dice.total

    def saveResult(directory=''):
        if directory == '':
            savetxt = open('savedResult.txt', 'a+')
        else:
            savetxt = open(os.path.join(directory, 'savedResult.txt'), 'a+')
        savetxt.write(str(Dice.result) + '\n')
        savetxt.close()

    def saveTotal(directory=''):
        if directory == '':
            savetxt = open('savedTotal.txt', 'a+')
        else:
            savetxt = open(os.path.join(directory, 'savedTotal.txt'), 'a+')
        savetxt.write(str(Dice.total) + '\n')
        savetxt.close()
