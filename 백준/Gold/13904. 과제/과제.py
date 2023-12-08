import sys
import heapq

input = sys.stdin.readline

arr = []
q = []

n = int(input())
result = 0

for i in range(n):
  day, score = map(int,input().split())
  arr.append((day,score))

arr.sort()

for i in range(n):
  if len(q) < i+1 and arr[i][0] > len(q):
    heapq.heappush(q,(arr[i][1],arr[i][0]))
  else:
    if q[0][0] < arr[i][1]:
      heapq.heappop(q)
      heapq.heappush(q,(arr[i][1],arr[i][0]))

for a, b in q:
  result += a

print(result)