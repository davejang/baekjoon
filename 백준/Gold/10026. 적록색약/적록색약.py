from collections import deque

N = int(input())
graph = []
visited = [[0 for col in range(N)] for row in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

area_1 = 0
area_2 = 0

for i in range(N):
    column = str(input())
    column = list(column)
    graph.append(column)

def bfs(a,b):
  queue = deque([])
  visited[a][b] = True
  queue.append((a,b))
  color = graph[a][b]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if graph[nx][ny] != color:
        continue
      if graph[nx][ny] == color and visited[nx][ny] != True:
        visited[nx][ny] = True
        queue.append((nx,ny))

for i in range(N):
  for j in range(N):
    if visited[i][j] != True:
      bfs(i,j)
      area_1 += 1
for i in range(N):
  for j in range(N):
    if graph[i][j] == 'G':
      graph[i][j] = 'R'
    visited[i][j] = 0
for i in range(N):
  for j in range(N):
    if visited[i][j] != True:
      bfs(i,j)
      area_2 += 1

print(area_1,area_2)
