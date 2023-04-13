from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([])
    queue.append((begin,0))
    
    while queue:
        cur, count = queue.popleft()
            
        if cur == target:
            return count

        for w in words:
            # 바뀌는 단어가 하나일 경우에만 이동
            dif = 0
            for i in range(len(cur)):
                if cur[i] != w[i]:
                    dif += 1
                        
            if dif == 1:
                queue.append((w,count+1))
    return 0