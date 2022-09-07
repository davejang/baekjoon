from collections import deque

N = int(input())

visited = [[0 for col in range(N)] for row in range(N)]
array = []
answer_list = []
counbt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
  col = list(str(input().strip()))
  array.append(col)
  
def bfs(a,b):
  number = 0
  queue = deque([])
  queue.append((a,b))
  visited[a][b] = True
  if array[a][b] == '1':
    number = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if array[nx][ny] == '1' and visited[nx][ny] != True:
        visited[nx][ny] = True
        number += 1
        queue.append((nx,ny))
  return number

for i in range(N):
  for j in range(N):
    if visited[i][j] != True and array[i][j] == '1':
      result = bfs(i,j)
      answer_list.append(result)
print(len(answer_list))
answer_list.sort()
for k in answer_list:
  print(k)