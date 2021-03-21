# https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    sek, mn, hh = 0, 0, 0
    for i in range(1, seconds + 1):
        sek += 1
        if sek == 60:
            mn += 1
            sek = 0
            if mn == 60:
                hh += 1
                mn = 0
    if len(str(sek)) < 2:
        sek = '0' + str(sek)
    if len(str(mn)) < 2:
        mn = '0' + str(mn)
    if len(str(hh)) < 2:
        hh = '0' + str(hh)

    return str(hh) + ':' + str(mn) + ':' + str(sek)
