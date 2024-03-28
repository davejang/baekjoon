import sys

input = sys.stdin.readline

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

data = []
n = int(input())
parents = [x for x in range(n+1)]
edges = []

for i in range(n):
    data.append(list(str(input())))

total = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 0:
            edges.append((0, i+1, j+1))
        else:
            if ord('a') <= ord(data[i][j]) <= ord('z'):
                edges.append((ord(data[i][j]) - ord('a') + 1, i+1, j+1))
                total += (ord(data[i][j]) - ord('a') + 1)
            elif ord('A') <= ord(data[i][j]) <= ord('Z'):
                edges.append((ord(data[i][j]) - ord('A') + 27, i+1, j+1))
                total += (ord(data[i][j]) - ord('A') + 27)

edges.sort()
for g in edges:
    cost, a, b = g
    if cost == 0:
        continue
    if find_parents(a) != find_parents(b):
        union(a, b)
        total -= cost
    else:
        continue

result = True
for i in range(1, n+1):
    if find_parents(i) != 1:
        result = False
        
if result:
    print(total)
else:
    print(-1)