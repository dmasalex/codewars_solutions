# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    dict_word = {}
    lst = []
    lst_dict = []
    for i in word:
        if i in dict_word:
            dict_word[i] += 1
        else:
            dict_word[i] = 1
    for i in range(len(words)):
        dict_words = {}
        for j in words[i]:
            if j in dict_words:
                dict_words[j] += 1
            else:
                dict_words[j] = 1
        lst_dict.append(dict_words)
    for i in range(len(lst_dict)):
        if lst_dict[i] == dict_word:
            lst.append(words[i])
    return lst
