import sys
from collections import deque

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
user = {}
user_count = 0

n, m, fuel = map(int,input().split())
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))
x, y = map(int,input().split())
x = x-1
y = y-1

for i in range(m):
  a, b, c, d = map(int,input().split())
  user[(a-1,b-1)] = (c-1,d-1)
for u in user:
  graph[u[0]][u[1]] = 2
  user_count += 1

# 택시와 승객 간 거리 계산 및 후보 승객 선택
def bfs(a,b):
  cand_list = []
  visited = [[0 for _ in range(n)] for _ in range(n)]
  q = deque()
  q.append((a,b,0))
  visited[a][b] = 1
  # 택시가 승객 위치에 있는 경우
  if graph[a][b] == 2:
    cand_list.append((a,b,0))

  while(q):
    x, y, fuel = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] != 1 and visited[nx][ny] == 0:
          visited[nx][ny] = 1
          q.append((nx,ny,fuel+1))
          # 승객 좌표 도달할 경우, 최단 거리 설정
          if graph[nx][ny] == 2:
            cand_list.append((nx,ny,fuel+1))

  if not cand_list:
    return 0, 0, -1
  cand_list.sort(key = lambda x:(x[2],x[0],x[1]))
  x, y, fuel = cand_list[0]
  # 승객 탑승 처리
  graph[x][y] = 0
  # 최단거리 승객과 소모 연료 return
  return x, y, fuel

def drive(a,b,c,d):
  visited = [[0 for _ in range(n)] for _ in range(n)]
  q = deque()
  q.append((a,b))
  visited[a][b] = 1

  while q:
    x, y = q.popleft()
    if x == c and y == d:
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] != 1 and visited[nx][ny] < 1:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx,ny))

  return visited[c][d] - 1

while user_count > 0:
  
  now_x, now_y, use_fuel = bfs(x,y)
  # 도달할 수 없는 경우
  if use_fuel == -1:
    fuel = -1
    break
  user_count -= 1

  fuel -= use_fuel
  if fuel <= 0:
    fuel = -1
    break

  pur_x, pur_y = user[(now_x,now_y)]
  use_fuel = drive(now_x,now_y,pur_x,pur_y)
  # 도달할 수 없는 경우
  if use_fuel < 0:
    fuel = -1
    break

  # 연료가 부족한 경우
  if fuel - use_fuel < 0:
    fuel = -1
    break
  else:
    fuel += use_fuel

  x, y = pur_x, pur_y

print(fuel)