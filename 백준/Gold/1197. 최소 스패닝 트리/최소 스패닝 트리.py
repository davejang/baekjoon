import sys

INF = int(1e9)

input = sys.stdin.readline
result = 0

v, e = map(int,input().split())
parent = [i for i in range(v+1)]
edge_list = []

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

for i in range(e):
  a, b, c = map(int,input().split())
  edge_list.append((a,b,c))

edge_list = sorted(edge_list,key = lambda x : x[2])

for e in edge_list:
  if find_parent(e[0]) == find_parent(e[1]):
    continue
  else:
    union(e[0],e[1])
    result += e[2]

print(result)