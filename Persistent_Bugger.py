# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    str_n = str(n)
    z, x, y = 0, 0, 1
    while True:
        z += 1
        if len(str_n) == 1:
            break
        else:
            for i in str_n:
                x = int(i)
                y = y * x
        str_n = str(y)
        y = 1
    return z - 1
