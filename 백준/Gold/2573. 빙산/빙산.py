import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
time = 0

n, m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

def bfs(a,b):
  count = graph[a][b]
  visited = [[0 for _ in range(m)] for _ in range(n)]
  q = deque()
  q.append((a,b))
  visited[a][b] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if graph[nx][ny] > 0 and visited[nx][ny] == 0:
        q.append((nx,ny))
        visited[nx][ny] = 1
        count += graph[nx][ny]
        
  return count

while True:
  time += 1
  
  for i in range(n):
    for j in range(m):
      count = 0
      if graph[i][j] > 0:
        for c in range(4):
          nx = i + dx[c]
          ny = j + dy[c]
          if graph[nx][ny] == 0:
            count += 1
        queue.append((i,j,count))
  
  while queue:
    x, y, count = queue.popleft()
    graph[x][y] = graph[x][y] - count
    if graph[x][y] < 0:
      graph[x][y] = 0
    if graph[x][y] > 0:
      a, b = x, y

  temp = 0
  for i in range(n):
    temp += sum(graph[i])
  if temp == 0:
    print(0)
    break

  if temp != bfs(a,b):
    print(time)
    break