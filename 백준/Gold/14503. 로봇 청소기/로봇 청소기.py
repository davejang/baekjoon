import sys

input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]
graph = []
clean_count = 0

n, m = map(int,input().split())
visited= [[0 for _ in range(m)] for _ in range(n)]

r, c, d = map(int,input().split())
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

visited[r][c] = 1
clean_count = 1

while True:
  flag = 0

  # 4방향 체크
  for i in range(4):
    nr = r + dx[i]
    nc = c + dy[i]
    if nr < 0 or nc < 0 or nr >= n or nc >= m:
      continue
    if graph[nr][nc] == 0 and visited[nr][nc] == 0:
      flag = 1
      break

  if flag == 0:
    nr = r - dx[d]
    nc = c - dy[d]
    if graph[nr][nc] == 1:
      print(clean_count)
      break
    else:
      r = nr
      c = nc
  if flag == 1:
    for i in range(4):
      d = (d+3)%4
      nr = r + dx[d]
      nc = c + dy[d]
      
      if nr < 0 or nc < 0 or nr >= n or nc >= m:
        continue
      if graph[nr][nc] == 1:
        continue
      if visited[nr][nc] == 0:
        r = nr
        c = nc
        visited[r][c] = 1
        clean_count += 1
        break