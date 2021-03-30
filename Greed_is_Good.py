# https://www.codewars.com/kata/5270d0d18625160ada0000e4

def score(dice):
    rez = 0
    if dice.count(1) >= 3:
        rez += 1000
        while True:
            dice.remove(1)
            if len(dice) == 2:
                break
    elif dice.count(6) >= 3:
        rez += 600
        while True:
            dice.remove(6)
            if len(dice) == 2:
                break
    elif dice.count(5) >= 3:
        rez += 500
        while True:
            dice.remove(5)
            if len(dice) == 2:
                break
    elif dice.count(4) >= 3:
        rez += 400
        while True:
            dice.remove(4)
            if len(dice) == 2:
                break
    elif dice.count(3) >= 3:
        rez += 300
        while True:
            dice.remove(3)
            if len(dice) == 2:
                break
    elif dice.count(2) >= 3:
        rez += 200
        while True:
            dice.remove(2)
            if len(dice) == 2:
                break
    for i in dice:
        if i == 1:
            rez += 100
        if i == 5:
            rez += 50
    return rez
