from collections import deque

m, n = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
days = 0
tomato_location = []

for i in range(n):
  graph.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      tomato_location.append((i,j))


queue = deque([])
for i in tomato_location:
  queue.append(i)
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if graph[nx][ny] == -1:
      continue
    if graph[nx][ny] == 0:
      graph[nx][ny] = graph[x][y] + 1
      queue.append((nx,ny))
day = 0
isBreak = False
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      day = -1
      isBreak = True
      break
    if day < graph[i][j]:
      day = graph[i][j]
  if isBreak == True:
    break

if day > 0:
  print(day-1)
else:
  print(day)