# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    if b == []:
        return a
    else:
        for i in b:
            if i in a:
                while i in a:
                    a.remove(i)
        return a
