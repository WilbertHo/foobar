import math

def answer(n):
    gauze = 0
    coins = n

    while coins:
        coins = coins - (int(math.floor(math.sqrt(coins))) ** 2)
        gauze += 1

    return gauze
