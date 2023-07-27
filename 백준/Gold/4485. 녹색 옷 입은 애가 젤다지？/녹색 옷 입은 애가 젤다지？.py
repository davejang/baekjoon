import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 1

def dijkstra(a,b):
  q = []
  heapq.heappush(q,(graph[a][b],a,b))
  distance[a][b] = graph[a][b]

  while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
        
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q,(cost,nx,ny))
      
while True:
  n = int(input())
  if n == 0:
    break
  graph = []
  for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))
  distance = [[INF for _ in range(n)] for _ in range(n)]
  dijkstra(0,0)
  
  min = distance[n-1][n-1]
  print("Problem %d: %d"%(count,min))
  count += 1