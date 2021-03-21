# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        x = 0
        for i in str(n):
            x += int(i)
        if len(str(x)) == 1:
            return x
        else:
            return digital_root(x)
