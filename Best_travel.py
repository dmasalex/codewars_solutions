import itertools


def choose_best_sum(t, k, ls):
    rez = 0
    lst = itertools.combinations(ls, k)
    new_lst = list(lst)
    for i in new_lst:
        x = sum(i)
        if rez < x <= t:
            rez = x
    if rez == 0:
        return None
    else:
        return rez
