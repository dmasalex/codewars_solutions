# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    lst = text.split()
    ay, rez = 'ay', ''
    punctuation = '.,():;!=-_@#><?*&%$'
    for i in lst:
        if i in punctuation:
            rez += i + ' '
        else:
            rez += i[1:] + i[0] + ay + ' '
    return rez[:-1]
