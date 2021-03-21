# https://www.codewars.com/kata/55e2adece53b4cdcb900006c

from decimal import Decimal
def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        rez = []
        sek_it = g / ((v2 - v1) / 60 / 60)
        s_it = Decimal(sek_it)
        s_it = int(s_it.quantize(Decimal('1.00')))
        h = s_it // 3600
        m = (s_it - h * 3600) // 60
        sek = s_it % 60
        rez.append(h)
        rez.append(m)
        rez.append(sek)
        return rez
