import sys
import heapq

input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n+1)]
edges = []
result = int(1e9)

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union(a,b):
  a = find_parent(a)
  b = find_parent(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in range(m):
  a, b, c = map(int,input().split())
  heapq.heappush(edges,(-c,a,b))

p1, p2 = map(int,input().split())

while edges:
  if find_parent(p1) == find_parent(p2):
    break
  cost, start, end = heapq.heappop(edges)
  
  if find_parent(start) == find_parent(end):
    continue
  else:
    union(start,end)
    result = cost
    
print(-result)