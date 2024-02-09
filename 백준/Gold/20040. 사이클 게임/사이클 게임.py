import sys

INF = int(1e9)

input = sys.stdin.readline

n, m = map(int,input().split())
time = 0
parent = [i for i in range(n)]

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
  time += 1
  a, b = map(int,input().split())
  if find_parent(a) == find_parent(b):
    print(time)
    exit(0)
  union(a,b)

print(0)