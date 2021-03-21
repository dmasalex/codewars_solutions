# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        itoq = names[0] + ' ' + "likes this"
        return itoq
    elif len(names) == 2:
        x, y = names[0], names[1]
        itog = x + ' ' + 'and' + ' ' + y + ' ' + 'like this'
        return itog
    elif len(names) == 3:
        x, y, z = names[0], names[1], names[2]
        x = x + ','
        itog = x + ' ' + y + ' ' + 'and' + ' ' + z + ' ' + 'like this'
        return itog
    else:
        x, y = names[0], names[1]
        x = x + ','
        z = str(len(names) - 2)
        itog = x + ' ' + y + ' ' + 'and' + ' ' + z + ' ' + 'others like this'
        return itog
