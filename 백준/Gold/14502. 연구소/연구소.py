from collections import deque
import copy

n, m = map(int,input().split())
array = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

for i in range(n):
  array.append(list(map(int,input().split())))

def virus():
  global answer
  temp_array = copy.deepcopy(array)

  queue = deque([])
  for r in range(n):
    for c in range(m):
      if temp_array[r][c] == 2:
        queue.append((r,c))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if temp_array[nx][ny] == 0:
        queue.append((nx,ny))
        temp_array[nx][ny] = 2

  count = 0
  for i in range(n):
    for j in range(m):
      if temp_array[i][j] == 0:
        count += 1
  #print(count)
  answer = max(answer,count)

def make_wall(count):
  if count == 3:
    virus()
    return

  for i in range(n):
    for j in range(m):
      if array[i][j] == 0:
        array[i][j] = 1
        make_wall(count+1)
        array[i][j] = 0

make_wall(0)
print(answer)