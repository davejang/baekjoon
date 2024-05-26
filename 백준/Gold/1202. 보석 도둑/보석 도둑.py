import sys
import heapq

input = sys.stdin.readline

n, k = map(int,input().split())
gems = []
bags = []
answer = 0

for i in range(n):
    m, v = map(int,input().split())
    heapq.heappush(gems,(m,v))
    
for i in range(k):
    bags.append(int(input()))
bags.sort()
tmp = []

for bag in bags:
    while gems and bag >= gems[0][0]:
        heapq.heappush(tmp, -heapq.heappop(gems)[1])
        
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not gems:
        break
    
print(answer)