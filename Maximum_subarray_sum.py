# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    max_m = 0
    while len(arr) != 0:
        n = 0
        while n != len(arr):
            tmp = sum(arr[n:])
            n += 1
            if tmp > max_m:
                max_m = tmp
        del arr[-1]
    return max_m
