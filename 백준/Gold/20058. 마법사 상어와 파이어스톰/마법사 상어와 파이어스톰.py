import sys
from collections import deque

input = sys.stdin.readline
graph = []
firestorm = []
dir = [(0,1),(1,0),(0,-1),(-1,0)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

n, q = map(int,input().split())
for i in range(2**n):
  graph.append(list(map(int,input().rstrip().split())))
firestorm = list(map(int,input().rstrip().split()))

# 얼음 감소
def ice_discount(x,y):
  count = 0
  if graph[x][y] == 0:
    return False
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 2**n and 0 <= ny < 2**n:
      if graph[nx][ny] != 0:
        count += 1

  if count < 3:
    return (x, y)

for l in firestorm:
  temp_graph = [[0 for _ in range(2**n)] for _ in range(2**n)]
  d = 0
  
  # (i,j) = 기준점
  for i in range(0,2**n,2**l):
    for j in range(0,2**n,2**l):
      # 격자 단위로 90도 회전
      for a in range(2**l):
        for b in range(2**l):
          temp_graph[i+b][j+2**l-a-1] = graph[i+a][j+b]
  graph = temp_graph.copy()

  discount_list = []
  for i in range(2**n):
    for j in range(2**n):
      if ice_discount(i,j):
        discount_list.append(ice_discount(i,j))

  for i, j in discount_list:
    graph[i][j] -= 1

result2 = 0
visited = [[0 for _ in range(2**n)] for _ in range(2**n)]

def bfs(a,b):
  ice = 1
  q = deque()
  visited[a][b] = 1
  q.append((a,b))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 2**n and 0 <= ny < 2**n and visited[nx][ny] == 0 and graph[nx][ny] != 0:
        ice += 1
        visited[nx][ny] = 1
        q.append((nx,ny))
  return ice
  
for i in range(2**n):
  for j in range(2**n):
    if visited[i][j] == 1 or graph[i][j] == 0: 
      continue
    result2 = max(result2,bfs(i,j))

for col in graph:
  result += sum(col)
print(result)
print(result2)