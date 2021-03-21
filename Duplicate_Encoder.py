# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    dict_w = {}
    ret = ''
    for i in word.lower():
        if i in dict_w:
            dict_w[i] += 1
        else:
            dict_w[i] = 1
    for i in word.lower():
        if dict_w[i] != 1:
            ret += ')'
        else:
            ret += '('
    return ret
