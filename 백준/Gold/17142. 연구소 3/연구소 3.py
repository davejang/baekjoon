import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)
result = INF

n, m = map(int,input().split())
graph = []

def bfs(virus_q,left_blank):
  global result
  visited = [[0 for _ in range(n)] for _ in range(n)]
  
  q = deque(virus_q)
  for i, j in q:
    visited[i][j] = 1

  while q:
    if left_blank == 0:
      break
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 범위 벗어나는 경우 continue
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      # 벽이거나 방문한 경우 continue
      if graph[nx][ny] == 1 or visited[nx][ny] >= 1:
        continue

      visited[nx][ny] = visited[x][y] + 1
      q.append((nx,ny))
      # 빈칸일 경우에만 left_blank 감소처리
      if graph[nx][ny] == 0:
        left_blank -= 1

  time = 0
  for i in range(n):
    for j in range(n):
      time = max(time,visited[i][j])

  if left_blank == 0:
    result = min(result,time-1)
  
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

virus_list = []
left_blank = 0
for i in range(n):
  for j in range(n):
    # 바이러스 위치 저장
    if graph[i][j] == 2:
      virus_list.append((i,j))
    # 빈칸의 개수 count
    if graph[i][j] == 0:
      left_blank += 1

# 바이러스 조합
virus_q = list(combinations(virus_list,m))

for q in virus_q:
  bfs(q,left_blank)

if result == INF:
  print(-1)
else:
  print(result)