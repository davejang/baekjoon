from collections import deque

n, m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
  string = str(input())
  row = []
  for j in range(m):
    row.append(int(string[j]))
  graph.append(row)

queue = deque([])
queue.append((0,0))
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if graph[nx][ny] == 0:
      continue
    if graph[nx][ny] == 1:
      graph[nx][ny] = graph[x][y] + 1
      queue.append((nx,ny))

print(graph[n-1][m-1])