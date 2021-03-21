# https://www.codewars.com/kata/55031bba8cba40ada90011c4

def is_sum_of_cubes(s):
    fig = '1234567890'
    f = ''
    l = 'Lucky'
    mas = []
    d = s.split()
    for i in d:
        mas.append(i)
    d = []
    for i in range(len(mas)):
        for j in mas[i]:
            if j in fig:
                f += j
        if f != '':
            d.append(int(f))
        f = ''
    mas = []
    for i in d:
        if len(str(i)) <= 3:
            mas.append(i)
        y = ''
        if len(str(i)) > 3:
            x = str(i)
            for j in x:
                y += j
                if len(y) == 3:
                    mas.append(y)
                    y = ''
            mas.append(y)
    d = []
    z = 0
    masik = []
    for i in mas:
        if str(i) != '':
            masik.append(i)
    for i in range(len(masik)):
        for k in str(masik[i]):
            x = int(k) ** 3
            z += x
        if z == int(masik[i]):
            d.append(z)
        z = 0
    sm = sum(d)
    mas = []
    if d == []:
        return "Unlucky"
    else:
        d.append(sm)
        d.append(l)
        for i in d:
            mas.append(str(i))
        return ' '.join(mas)
