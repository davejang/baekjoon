from collections import deque

n = int(input())
array = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
size = 2
time = 0
feed = 0

for i in range(n):
  array.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if array[i][j] == 9:
      x = i
      y = j

def bfs(a,b):
  global size
  visited = [[0 for col in range(n)] for row in range(n)]
  distance = [[0 for col in range(n)] for row in range(n)]
  queue = deque([])
  queue.append((a,b))
  can_eat = []
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if visited[nx][ny] == True:
        continue
      if array[nx][ny] <= size:
        queue.append((nx,ny))
        visited[nx][ny] = True
        distance[nx][ny] = distance[x][y] + 1
        if array[nx][ny] < size and array[nx][ny] != 0:
          can_eat.append((nx,ny,distance[nx][ny]))
  return sorted(can_eat,key= lambda x:(-x[2],-x[0],-x[1]))

while True:
  shark_info = bfs(x,y)
  if len(shark_info) == 0: # Null
    print(time)
    break
  shark_x, shark_y, distance = shark_info.pop()
  time += distance
  array[x][y] = 0
  array[shark_x][shark_y] = 0
  x = shark_x
  y = shark_y
  feed += 1
  if feed == size:
    size += 1
    feed = 0