from collections import deque

n, m, k = map(int,input().split())
arr = [[0 for col in range(m)] for row in range(n)]
visited = [[0 for col in range(m)] for row in range(n)]
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
gar_list = []
for i in range(k):
  x, y = map(int,input().split())
  gar_list.append((x-1,y-1))
  arr[x-1][y-1] = 1

def bfs(a,b):
  queue = deque([])
  queue.append((a,b))
  size = 1
  visited[a][b] = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny <0 or nx >= n or ny >= m:
        continue
      if arr[nx][ny] == 0:
        continue
      if visited[nx][ny] == 0:
        queue.append((nx,ny))
        visited[nx][ny] = 1
        size += 1

  return size

for x, y in gar_list:
  answer = max(answer,bfs(x,y))

print(answer)