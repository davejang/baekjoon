import sys
import heapq

input = sys.stdin.readline

# 최소 스패닝 트리를 구한 후 가장 긴 경로를 끊는다

def find_parent(x):
  if parents[x] != x:
    parents[x] = find_parent(parents[x])
  return parents[x]

def union(a,b):
  a = find_parent(a)
  b = find_parent(b)

  if a < b:
    parents[b] = a
  else:
    parents[a] = b

n, m = map(int,input().split())
parents = [i for i in range(n+1)]
heap = []
result = 0
last = 0

for i in range(m):
  a, b, c = map(int,input().split())
  heapq.heappush(heap,(c,a,b))

while heap:
  c, a, b = heapq.heappop(heap)
  if find_parent(a) == find_parent(b):
    continue
  union(a,b)
  result += c
  last = max(last,c)

print(result-last)