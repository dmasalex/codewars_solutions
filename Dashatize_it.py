# https://www.codewars.com/kata/58223370aef9fc03fd000071

def dashatize(n):
    if isinstance(n, int) == False:
        return "None"
    else:
        n = str(n)
        for i in range(len(n)):
            if n[0] == '-':
                n = n[1:]
        mas = []
        for i in range(len(n)):
            if int(n[i]) % 2 == 0:
                mas.append(n[i])
            else:
                if mas != [] and mas[-1] == '-':
                    mas.append(n[i])
                    mas.append('-')
                else:
                    mas.append('-')
                    mas.append(n[i])
                    mas.append('-')
        if mas[-1] == '-':
            del mas[-1]
        if mas[0] == '-':
            del mas[0]
        my_str = ''.join(mas)
        return my_str
