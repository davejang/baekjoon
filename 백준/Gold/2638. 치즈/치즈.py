import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
time = 0

n, m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

def search_cheese():
  temp = []
  result = []
  visited = [[0 for _ in range(m)] for _ in range(n)]
  q = deque()
  q.append((0,0))
  visited[0][0] = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[x][y] == 0:
        if graph[nx][ny] == 0:
          q.append((nx,ny))
        else:
          temp.append((nx,ny))

        visited[nx][ny] = 1

  for x, y in temp:
    count = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if graph[nx][ny] == 0 and visited[nx][ny] == 1:
        count += 1
      if count >= 2:
        break
    if count >= 2:
      result.append((x,y))
            
  return result

while True:
  time += 1
  cheese_list = search_cheese()
  for x, y in cheese_list:
    graph[x][y] = 0

  check = 0
  for i in graph:
    check += sum(i)
  if check == 0:
    break

print(time)