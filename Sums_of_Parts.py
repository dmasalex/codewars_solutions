# https://www.codewars.com/kata/5ce399e0047a45001c853c2b

def parts_sums(ls):
    lst = []
    sum_ls = sum(ls)
    lst.append(sum_ls)
    for i in range(len(ls)):
        sum_ls -= ls[i]
        lst.append(sum_ls)
    return lst
