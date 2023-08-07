import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
  arr = list(map(int,input().rstrip().split()))
  for a in arr:
    if len(q) < n:
      heapq.heappush(q,a)
    else:
      if q[0] < a:
        heapq.heappop(q)
        heapq.heappush(q,a)

print(q[0])