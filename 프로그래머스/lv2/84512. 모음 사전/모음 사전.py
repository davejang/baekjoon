from itertools import product

def solution(word):
    word_dict = []
    for i in range(1,6):
        word_dict += list(''.join(p) for p in product(['A','E','I','O','U'],repeat=i))
    word_dict.sort()
    for i in range(len(word_dict)):
        if word_dict[i] == word:
            answer = i + 1
            break
    return answer