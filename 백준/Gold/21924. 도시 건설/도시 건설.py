import sys

input = sys.stdin.readline

n, m = map(int,input().split())

edges = []
parents = [i for i in range(n+1)]
min_cost = 0
total_cost = 0

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(a,b):
    a = find_parents(a)
    b = find_parents(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(m):
    a, b, c = map(int,input().split())
    total_cost += c
    edges.append((c,a,b))
    
edges.sort(key=lambda x:x[0])

for c, a, b in edges:
    if find_parents(a) == find_parents(b):
        continue
    union(a,b)
    min_cost += c

temp = 0
for i in range(1,n+1):
    if parents[i] == i:
        temp += 1

if temp > 1:
    print(-1)
else:
    print(total_cost - min_cost)