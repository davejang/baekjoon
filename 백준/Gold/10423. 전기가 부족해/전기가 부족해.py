import sys

input = sys.stdin.readline

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(a,b):
    a = find_parents(a)
    b = find_parents(b)
    
    if a in plant:
        parents[b] = a
    elif b in plant:
        parents[a] = b
    elif a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m, k = map(int,input().split())
parents = [i for i in range(n+1)]
plant = list(map(int,list(input().split())))
edges = []
min_cost = 0

for i in range(m):
    u, v, w = map(int,input().split())
    edges.append((w,u,v))
    
edges.sort(key=lambda x:x[0])

for w, u, v in edges:
    if find_parents(u) in plant and find_parents(v) in plant:
        continue
    if find_parents(u) == find_parents(v):
        continue
    
    union(u,v)
    min_cost += w
    
print(min_cost)