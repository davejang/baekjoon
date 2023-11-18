import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int,input().split())
graph = []
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
result = 0

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

q = deque()

for i in range(h):
  hight = []
  for j in range(n):
    hight.append(list(map(int,input().rstrip().split())))
  graph.append(hight)

for a in range(h):
  for b in range(n):
    for c in range(m):
      if graph[a][b][c] == 1 and visited[a][b][c] == 0:
        q.append((a,b,c))
        visited[a][b][c] = 1

def bfs():
  while q:
    x, y, z = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
        continue

      if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
        q.append((nx,ny,nz))
        visited[nx][ny][nz] = 1
        graph[nx][ny][nz] = graph[x][y][z] + 1

bfs()

for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        result = max(result, max(b))

print(result-1)