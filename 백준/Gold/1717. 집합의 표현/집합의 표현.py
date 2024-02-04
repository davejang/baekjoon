import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

def get_parent(x):
  if parent[x] != x:
    parent[x] = get_parent(parent[x])
  return parent[x]

def union_parent(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a < b:
      parent[b] = a
  else:
      parent[a] = b      

for i in range(m):
  opr, a, b = map(int,input().split())
  if opr == 0:
    union_parent(a,b)
  else:
    if get_parent(a) == get_parent(b):
      print("YES")
    else:
      print("NO")