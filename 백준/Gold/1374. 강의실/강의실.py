import sys
import heapq

input = sys.stdin.readline
count = 1
temp = 0
q = []
count = 0

n = int(input())
arr = []
for i in range(n):
  number, start, end = map(int,input().split())
  heapq.heappush(arr,(start,end))

arr.sort(key = lambda x:x[0])

for lecture in arr:
  while q and q[0] <= lecture[0]:
    heapq.heappop(q)
  heapq.heappush(q,(lecture[1]))
  count = max(count,len(q))

print(count)