import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
s = deque()
t = ""
count = 0

for i in range(n):
    c = str(input().rstrip())
    s.append(c)
    
while s:
    left = 0
    right = len(s) - 1
    flag = 0
    
    while left <= right:       
        if s[left] > s[right]:
            flag = 0
            break
        elif s[left] < s[right]:
            flag = 1
            break
        
        left += 1
        right -= 1 
    
    if flag == 0:
        t += s.pop()
    elif flag == 1:
        t += s.popleft()
                    
    count += 1
    
    if count % 80 == 0:
        t += '\n'
    
print(t)