import sys
import heapq

input = sys.stdin.readline

q = []

n = int(input())
left = []
right = []

for i in range(n):
  number = int(input())
  
  if len(left) == len(right):
    heapq.heappush(left,-number)
  else:
    heapq.heappush(right,number)

  if right and right[0] < -left[0]:
    r = heapq.heappop(right)
    l = heapq.heappop(left)
    heapq.heappush(left,-r)
    heapq.heappush(right,-l)

  print(-left[0])