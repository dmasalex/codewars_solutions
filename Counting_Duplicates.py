# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    dict_text = {}
    for i in text.lower():
        if i in dict_text:
            dict_text[i] += 1
        else:
            dict_text[i] = 1
    rez = 0
    for k, v in dict_text.items():
        if v >= 2:
            rez += 1

    return rez
