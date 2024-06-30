import sys
import heapq

input = sys.stdin.readline

n = int(input())
paths = []
for i in range(n):
    h, o = map(int,input().split())
    if h > o:
        h, o = o, h
    paths.append((h,o))
d = int(input())
result = 0

paths.sort(key=lambda x:x[1])

q = []

for path in paths:
    if path[1] - path[0] > d:
        continue
    if not q:
        heapq.heappush(q,path)
    else:
        while q[0][0] < path[1] - d:
            heapq.heappop(q)
            if not q:
                break
        heapq.heappush(q,path)
    result = max(result,len(q))
    
print(result)