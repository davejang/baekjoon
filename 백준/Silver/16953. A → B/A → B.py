import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int,input().split())
result = -1

q = deque([])
q.append((1,a))

while q:
  count, x = q.popleft()
  if x == b:
    result = count
    break

  if x * 2 <= b:
    q.append((count+1,x * 2))
  if x * 10 + 1 <= b:
    q.append((count+1,x * 10 + 1))

print(result)