from itertools import permutations
import re

def solution(user_id, banned_id):
    result = []
    banned_id = [i.replace("*",".") for i in banned_id]
    
    for case in permutations(user_id,len(banned_id)):
        case = list(case)
        flag = True
        
        for i in range(len(case)):
            if len(case[i]) != len(banned_id[i]):
                flag = False
                break
            if not re.match(banned_id[i],case[i]):
                flag = False
                break

        if flag:
            if sorted(case) not in result:
                result.append(sorted(case))

    answer = len(result)
    return answer