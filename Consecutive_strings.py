# https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(strarr, k):
    lst = []
    x = 0
    n = k - 1
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    else:
        for i in range(len(strarr) - n):
            lst_m = strarr[x:k]
            str_k = ''
            str_k = ''.join(lst_m)
            lst.append(str_k)
            x += 1
            k += 1

        lst_x = []
        for i in lst:
            lst_x.append(len(i))
        return lst[lst_x.index(max(lst_x))]
