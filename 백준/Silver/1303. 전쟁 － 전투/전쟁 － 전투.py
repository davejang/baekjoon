from collections import deque

n, m = map(int,input().split())
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
my_power = 0
other_power = 0

visited = [[0 for col in range(n)] for row in range(m)]
for i in range(m):
  arr.append(list(str(input())))

def bfs(a,b):
  global my_power
  global other_power
  
  queue = deque([])
  queue.append((a,b))
  team = arr[a][b]
  count = 1
  visited[a][b] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny <0 or nx >= m or ny >=n:
        continue
      if arr[nx][ny] != team:
        continue
      if visited[nx][ny] == 0:
        queue.append((nx,ny))
        visited[nx][ny] = True
        count += 1
  if team == 'W':
    my_power += count*count
  else:
    other_power += count*count

for i in range(m):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i,j)

print(my_power,other_power)