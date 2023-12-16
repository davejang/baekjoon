import sys
from collections import defaultdict

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
input = sys.stdin.readline
time = 0

n, k = map(int, input().split())
arr = []
graph = [[[] for _ in range(n)] for _ in range(n)]
position = defaultdict(int)

for i in range(n):
  arr.append(list(map(int, input().rstrip().split())))

for i in range(k):
  col, row, dir = map(int, input().split())
  position[i+1] = [col-1, row-1, dir]
  graph[col-1][row-1].append(i+1)

def move(x,y,nx,ny):
  if arr[nx][ny] == 0:
    for item in graph[x][y]:
      position[item][0] = nx
      position[item][1] = ny

    graph[nx][ny] += graph[x][y]
    graph[x][y] = []

  elif arr[nx][ny] == 1:
    graph[x][y].reverse()
    
    for item in graph[x][y]:
      position[item][0] = nx
      position[item][1] = ny
    
    graph[nx][ny] += graph[x][y]
    graph[x][y] = []

while time < 1000:
  time += 1
  
  for i in range(1, k+1):
    x, y, dir = position[i]
    # 가장 밑에 있는 말이 아닐 경우 skip
    if graph[x][y][0] != i:
      continue

    nx = x + dx[dir]
    ny = y + dy[dir]

    # 흰색 / 빨간색
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
      move(x,y,nx,ny)
    # 파란색 / 범위 밖
    else:
      if dir == 1:
        dir = 2
      elif dir == 2:
        dir = 1
      elif dir == 3:
        dir = 4
      elif dir == 4:
        dir = 3
      
      position[i][2] = dir

      nx = x + dx[dir]
      ny = y + dy[dir]

      if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
        move(x,y,nx,ny)

  for i in range(n):
    for j in range(n):
      if len(graph[i][j]) >= 4:
        print(time)
        exit()

print(-1)