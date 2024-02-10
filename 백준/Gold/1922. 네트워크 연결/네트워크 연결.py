import sys

INF = int(1e9)

input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
ans = 0

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

network = []

for i in range(m):
  a, b, c = map(int,input().split())
  network.append((c,a,b))

network.sort()

for cost, a, b in network:
  if find_parent(a) == find_parent(b):
    continue
  else:
    union(a,b)
    ans += cost

print(ans)