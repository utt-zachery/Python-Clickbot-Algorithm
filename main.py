import random
import time

from pynput.mouse import Button, Controller
from decimal import Decimal

r1 = 0.5 #how random clicks should be (0 being completely evenly spaced clicks, 1 being completely random spacing)
count1 = 10 #amount of clicks per second
numRunSeconds = 10 #number of seconds the bot should run for

#given an r value from 0-1 indicating an arbitrary level of "random" spread and a number of clicks to place per second, the genStructure returns the amount of seconds between clicks using a pseudorandom spread distribution, controlling the degree of "randomness" (variation) in the data set

def genStructure(r, count):
    vals = [None] * count
    sum = 1000
    #total amount of seconds to be divided into count groups
    for i in range(0, count):
        vals[i] = random.randint(0, sum)
    vals[count - 1] = sum
    vals.sort()

    for i in reversed(range(1, count)):
        vals[i] -= vals[i - 1]

    for i in range(0, count):
        ++vals[i]

    disaray = 0
    for i in range(0, count):
        disaray = disaray + abs(vals[i] - (1000.0 / count))
    disaray = disaray / 2
    correction = ((1 - r) * disaray)
    period = 1000.0 / count
    for i in range(0, count):
        if (vals[i] > period):
            vals[i] = (
                vals[i] - (correction * abs(abs(vals[i] - period) / disaray)))
        else:
            vals[i] = (
                vals[i] + (correction * abs(abs(vals[i] - period) / disaray)))
    return vals


print(genStructure(1, 10))


mouse = Controller()

temp_list = []


for a in range (0, numRunSeconds):
    start = time.time()
    currentData = genStructure(r1, count1)
    for a in range(0, len(currentData)):
        quickTime = time.time()
        mouse.press(Button.left)
        mouse.release(Button.left)
        if (float((Decimal(presplit[a]) / Decimal(1000))) - (time.time() - quickTime) > 0):
            time.sleep(float((Decimal(presplit[a]) / Decimal(1000))) - (time.time() - quickTime))

