import sys
import heapq

input = sys.stdin.readline

n = int(input())
result = 0
q = []
dp = [0]
for i in range(n):
  heapq.heappush(q,int(input()))

while q:
  if len(q) >= 2:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    dp.append(a+b)
    heapq.heappush(q,a+b)
  else:
    heapq.heappop(q)

print(sum(dp))