def solution(n, words):
    answer = []
    used_word = [words[0]]
    last_word = words[0]
    now = 1
    turn = 1
    
    for i in range(1,len(words)):
        now += 1
        if now > n:
            now = 1
            turn += 1
        
        if words[i] in used_word:
            answer = [now,turn]
            break
        elif words[i][0] != last_word[-1]:
            answer = [now,turn]
            break
        else:
            used_word.append(words[i])
            last_word = words[i]
            answer = [0,0]
        
    
    
    return answer