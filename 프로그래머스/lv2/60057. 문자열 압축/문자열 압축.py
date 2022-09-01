from collections import deque

def solution(s):
    answer = len(s)
    string_length = len(s)
    for i in range(1,string_length + 1):
        array = [s[j:j+i] for j in range(0,len(s),i)]
        queue = deque([])
        temp = 1
        for k in range(len(array)):
            if len(queue) == 0:
                queue.append(array[k])
            elif queue[0] == array[k]:
                temp += 1
                if k == len(array) - 1 and temp > 1:
                    a = queue.popleft()
                    a = str(temp)+a
                    queue.appendleft(a)
                continue
            else:
                if temp > 1:
                    a = queue.popleft()
                    a = str(temp)+a
                    queue.appendleft(a)
                    temp = 1
                queue.appendleft(array[k])
        string = ''.join(s for s in queue)
        length = len(string)
        if length < answer:
            answer = length

    return answer