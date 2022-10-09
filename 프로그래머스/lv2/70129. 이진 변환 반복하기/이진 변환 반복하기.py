def solution(s):
    bi_change_count = 0
    zero_del_count = 0
    
    while True:
        bi_change_count += 1
        new_word = []
        for c in s:
            if c == '1':
                new_word.append(c)
            else:
                zero_del_count += 1
        length = len(new_word)
        
        new_word = []
        while length >= 1:
            if length % 2 == 0:
                new_word.append('0')
            else:
                new_word.append('1')
            length = length // 2
        
        new_word.reverse()
        s = ''.join(new_word)
        if s == '1':
            break
    answer = [bi_change_count,zero_del_count]
    return answer