from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int,input().split())
graph = []
visited = [[-1 for col in range(m)] for row in range(n)]

for i in range(n):
  graph.append(list(map(int,input().split())))

def bfs(a,b):
  queue = deque([])
  queue.append((a,b))
  visited[a][b] = 0
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        visited[nx][ny] = 0
      elif visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx,ny))

for i in range(n):
    for k in range(m):
        if graph[i][k] == 2 and visited[i][k]== -1:
            bfs(i,k)

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      print(0,end = ' ')
    else:
      print(visited[i][j],end = ' ')
  print()
        