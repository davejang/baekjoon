def solution(dartResult):
    stack = []
    answer = 0
    
    for idx, c in enumerate(dartResult, start=1):
        if c == 'S':
            stack[-1] **= 1
            
        elif c == 'D':
            stack[-1] **= 2
            
        elif c == 'T':
            stack[-1] **= 3
            
        elif c == '*':
            stack[-1] *= 2
            if len(stack) >= 2:
                stack[-2] *= 2
                
        elif c == '#':
            stack[-1] *= -1
            
        else:
            if dartResult[idx-1:idx+1] == '10':
                stack.append(10)
            elif dartResult[idx-2:idx] != '10':
                stack.append(int(c))
                
    return sum(stack)