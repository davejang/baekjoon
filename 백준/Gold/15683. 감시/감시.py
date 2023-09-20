import sys
import copy

input = sys.stdin.readline

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

min_result = int(1e9)
graph = []
# cctv tree
cctv_list = []
# cctv 종류 별 방향
cctv_dir = [
  [],
  [[0],[1],[2],[3]],
  [[0,2],[1,3]],
  [[0,1],[1,2],[2,3],[3,0]],
  [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
  [[0,1,2,3]]
]

n, m = map(int,input().split())
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

for i in range(n):
  for j in range(m):
    if 1 <= graph[i][j] <= 5:
      cctv_list.append((i,j,graph[i][j]))

def fill(graph,dir,x,y):
  for i in dir:
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        break
      if graph[nx][ny] == 6:
        break
      if graph[nx][ny] == 0:
        graph[nx][ny] = -1

def dfs(depth,graph):
  global min_result
  if depth == len(cctv_list):
    cur_result = 0
    for i in range(n):
      for j in range(m):
        if graph[i][j] == 0:
          cur_result += 1

    min_result = min(min_result,cur_result)
    return

  x, y, cctv_type = cctv_list[depth]
  graph_temp = copy.deepcopy(graph)
  for dir in cctv_dir[cctv_type]:
    fill(graph_temp,dir,x,y)
    # dfs
    dfs(depth+1,graph_temp)
    # graph 초기화
    graph_temp = copy.deepcopy(graph)

dfs(0,graph)
print(min_result)