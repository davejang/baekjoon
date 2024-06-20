import sys

input = sys.stdin.readline
INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m, t, d = map(int,input().split())
distance = [[INF for _ in range(m*n)] for _ in range(m*n)]
graph = []
result = 0

def set_position(p):
    if 'a' <= p <= 'z':
        p = ord(p) - 71
    elif 'A' <= p <= 'Z':
        p = ord(p) - 65
        
    return p

for i in range(n):
    graph.append(list(str(input().rstrip())))
    
for i in range(n):
    for j in range(m):
        graph[i][j] = set_position(graph[i][j])
        
for i in range(n*m):
    for j in range(n*m):
        if i == j:
            distance[i][j] = 0
            
for i in range(n*m):
    x1, y1 = i // m, i % m
    for dir in range(4):
        x2 = x1 + dx[dir]
        y2 = y1 + dy[dir]
        j = x2 * m + y2
        
        if 0 <= x2 < n and 0 <= y2 < m:
            p1 = graph[x1][y1]
            p2 = graph[x2][y2]

            if abs(p1 - p2) > t:
                continue
            
            if p1 >= p2:
                distance[i][j] = 1
            else:
                distance[i][j] = (p2 - p1) ** 2
            
for k in range(n*m):
    for i in range(n*m):
        for j in range(n*m):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
            
ans = graph[0][0]

for i in range(n*m):
    if distance[0][i] + distance[i][0] <= d:
        ans = max(ans,graph[i//m][i%m])

print(ans)
