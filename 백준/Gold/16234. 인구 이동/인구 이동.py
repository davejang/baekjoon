import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int,input().split())
array = []
day = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque([])
  union_list = []
  population = array[x][y]
  queue.append((x,y))
  union_list.append((x,y))
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= n or ny >= n or nx < 0 or ny < 0:
        continue
      if visited[nx][ny] != True and abs(array[x][y] - array[nx][ny]) >= l and abs(array[x][y] - array[nx][ny]) <= r:
        queue.append((nx,ny))
        union_list.append((nx,ny))
        population += array[nx][ny]
        visited[nx][ny] = True
  union_count = len(union_list)
  for a,b in union_list:
    array[a][b] = population // union_count
  if union_count == 1:
    not_union[union_list[0][0]][union_list[0][1]] = 1
  
for i in range(n):
  array.append(list(map(int,input().split())))

while True:
  visited = [[0 for col in range(n)] for row in range(n)]
  not_union = [[0 for col in range(n)] for row in range(n)]
  end = [[1 for col in range(n)] for row in range(n)]
  for a in range(n):
    for b in range(n):
      if visited[a][b] != True:
        bfs(a,b)
  if not_union == end:
    print(day)
    break
  day += 1