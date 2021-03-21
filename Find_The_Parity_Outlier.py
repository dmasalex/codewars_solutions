# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    lst_even = []
    lst_odd = []
    for i in integers:
        if i % 2 == 0:
            lst_even.append(i)
        else:
            lst_odd.append(i)
    if len(lst_even) >= 2:
        for i in lst_odd:
            return i
    else:
        for i in lst_even:
            return i
