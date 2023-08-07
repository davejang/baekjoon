import sys
import heapq

input = sys.stdin.readline

n, m = map(int,input().split())
q = list(map(int,input().rstrip().split()))
heapq.heapify(q)
for i in range(m):
  x = heapq.heappop(q)
  y = heapq.heappop(q)
  heapq.heappush(q,x+y)
  heapq.heappush(q,x+y)

print(sum(q))