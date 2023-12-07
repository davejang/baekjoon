import sys
import heapq

input = sys.stdin.readline

n = int(input())
room = []
q = []

for i in range(n):
  start, end = map(int,input().split())
  room.append((start,end))
room.sort()

for i in range(n):
  if not q:
    heapq.heappush(q,(room[i][1],room[i][0]))
  else:
    if room[i][0] < q[0][0]:
      heapq.heappush(q,(room[i][1],room[i][0]))
    else:
      heapq.heappop(q)
      heapq.heappush(q,(room[i][1],room[i][0]))

print(len(q))