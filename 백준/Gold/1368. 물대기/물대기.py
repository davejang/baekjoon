import sys

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
        
n = int(input())
parents = [i for i in range(n+1)]
edges = []
result = 0
count = 0

for i in range(1,n+1):
    w = int(input())
    edges.append((w, 0, i))
    
for i in range(1,n+1):
    row = list(map(int,input().split()))
    for j in range(i+1,n+1):
        edges.append((row[j-1], i, j))
            
edges.sort()

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        count +=1
        result += cost
        # if count >= n:
        #     break
    
print(result)