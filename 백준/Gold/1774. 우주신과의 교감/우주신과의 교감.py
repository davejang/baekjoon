import sys
import math

input = sys.stdin.readline

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
cost = [[0 for _ in range(n+1)] for _ in range(n+1)]
point = [(0,0)]
exist_path = []
edges = []
result = 0

for i in range(n):
    x, y = map(int,input().split())
    point.append((x,y))
    
for i in range(1,n+1):
    for j in range(i+1,n+1):
        cost[i][j] = math.sqrt((point[i][0]-point[j][0])**2 + (point[i][1]-point[j][1])**2)
        edges.append((cost[i][j], i, j))
    
for i in range(m):
    x, y = map(int,input().split())
    exist_path.append((x,y))
    union(x,y)
    
edges.sort()

for cost, x, y in edges:
    if find_parent(x) != find_parent(y):
        union(x,y)
        result += cost
        
print("{:.2f}".format(result))