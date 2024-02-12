import sys

input = sys.stdin.readline

t = int(input())

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
 
for i in range(t):
  print(f"Scenario {i+1}:")
  n = int(input())
  k = int(input())
  parent = [j for j in range(n+1)]

  for _ in range(k):
    a, b = map(int,input().split())
    union(a,b)

  m = int(input())

  for _ in range(m):
    u, v = map(int,input().split())
    if find_parent(u) == find_parent(v):
      print(1)
    else:
      print(0)

  print()