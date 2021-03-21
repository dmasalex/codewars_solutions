# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    my_list = sentence.split(' ')
    for i in range(len(my_list)):
        if len(my_list[i]) >= 5:
            x = my_list[i]
            world = x[::-1]
            del my_list[i]
            my_list.insert(i, world)
    return ' '.join(my_list)
