# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    for key in recipe:
        if key not in available:
            return 0
    res = 0
    while True:
        for key in recipe:
            netto = available[key] - recipe[key]
            if netto < 0:
                return res
            available[key] = netto
        res += 1
