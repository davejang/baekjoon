import sys
import math

input = sys.stdin.readline

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

n = int(input())
parents = [i for i in range(n+1)]
stars = []
edges = []
result = 0

for i in range(n):
    x, y = map(float,input().split())
    stars.append((x,y))
    
for i in range(n-1):
    for j in range(i+1, n):
        cost = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edges.append((cost,i,j))
        
edges.sort()

for cost, x, y in edges:
    if find_parents(x) == find_parents(y):
        continue
    union(x,y)
    result += cost
    
print(round(result,2))