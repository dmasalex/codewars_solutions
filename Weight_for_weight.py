# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_weight(strng):
    lst = strng.split(' ')
    my_dict = {}
    rez = ''
    for i in range(len(lst)):
        x = 0
        for j in lst[i]:
            x += int(j)
        if x in my_dict:
            my_dict[x].append(lst[i])
        else:
            my_dict[x] = [lst[i]]
    lst = list(my_dict.keys())
    lst.sort()

    for i in lst:
        ls = my_dict[i]
        ls.sort()
        rz = ' '.join(ls)
        rez += rz + ' '

    return rez[:-1]
