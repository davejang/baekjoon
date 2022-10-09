def solution(s):
    answer = ''
    word_list = s.split(' ')
    JadenCase = []
    for word in word_list:
        word = word.capitalize()
        JadenCase.append(word)
    answer = ' '.join(JadenCase)

    return answer