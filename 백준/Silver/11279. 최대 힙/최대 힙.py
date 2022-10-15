import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
  num = int(input())
  if num == 0:
    if not heap:
      print(0)
    else:
      print(-1 * heapq.heappop(heap))
  else:
    heapq.heappush(heap,-num)