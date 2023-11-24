import sys
import heapq

input = sys.stdin.readline
q = []

n, l = map(int,input().split())
arr = list(map(int,input().rstrip().split()))

for i in range(n):
  
  heapq.heappush(q,(arr[i],i))

  while True:
    value, index = q[0]
    if i-l+1 <= index <= i:
      print(value,end = " ")
      break
    else:
      heapq.heappop(q)