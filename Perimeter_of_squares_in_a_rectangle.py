def perimeter(n):
    my_lst = [1, 1]
    for _ in range(2, n + 1):
        my_lst.append(my_lst[-1] + my_lst[-2])
    return 4 * sum(my_lst)
