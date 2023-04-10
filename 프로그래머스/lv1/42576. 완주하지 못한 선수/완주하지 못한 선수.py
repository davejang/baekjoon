def solution(participant, completion):
    hashmap = {}
    sumHash = 0
    
    # hashmap 생성 및 sumhash 계산
    for p in participant:
        hashmap[hash(p)] = p
        sumHash += hash(p)
        
    # completion hash 값들을 sumHash에서 모두 빼면 완주하지 못한 한 명의 해시값이 나온다
    for c in completion:
        sumHash -= hash(c)
        
    # 완주하지 못한 한 사람의 hash = sumHash
    return hashmap[sumHash]