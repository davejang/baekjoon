import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = INF

def bfs(a,b):
  global result
  q = deque([])
  q.append((1,a,b))
  visited[a][b] = 1

  for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            q.append((0, i, j))

  # base case
  if a == 0 or b == 0 or a == r - 1 or b == c - 1:
    result = 1
    return

  while q:
    type, x, y = q.popleft()

    if type == 1 and (x == 0 or y == 0 or x == r - 1 or y == c - 1) and graph[x][y] == '.':
      result = visited[x][y]
      break

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == '#': 
        continue
        
      if visited[nx][ny] == 0 and graph[nx][ny] == '.' and type == 1:
        visited[nx][ny] = visited[x][y] + 1
        q.append((1,nx,ny))
      elif graph[nx][ny] != 'F' and type == 0:
        graph[nx][ny] = 'F'
        q.append((0,nx,ny))

r, c = map(int,input().split())
graph = []
for i in range(r):
  graph.append(list(str(input().rstrip())))
visited = [[0 for _ in range(c)] for _ in range(r)]
fire_visited = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
  for j in range(c):
    if graph[i][j] == 'J':
      bfs(i,j)
      break

if result == INF:
  print('IMPOSSIBLE')
else:
  print(result)