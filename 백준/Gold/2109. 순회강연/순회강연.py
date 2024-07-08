import sys
import heapq

input = sys.stdin.readline

n = int(input())
request = []
result = 0
for i in range(n):
    p, d = map(int,input().split())
    request.append((d,p))
request.sort(key = lambda x:(x[0],-x[1]))

q = []
for d, p in request:
    if not q or len(q) < d:
        heapq.heappush(q,(p,d))
    else:
        if q[0][0] < p:
            heapq.heappop(q)
            heapq.heappush(q,(p,d))

for p, d in q:
    result += p

print(result)