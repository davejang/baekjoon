import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra(a,b):
  q = []
  heapq.heappush(q,(0,a,b))
  distance[a][b] = 0
  
  while q:
    dist, x, y = heapq.heappop(q)
    
    if distance[x][y] < dist:
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= m or ny >= n:
        continue

      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q,(cost,nx,ny))

n, m = map(int,input().split())
graph = []
distance = [[INF for _ in range(n)] for _ in range(m)]
for i in range(m):
  graph.append(list(map(int,input().rstrip())))

dijkstra(0,0)
print(distance[m-1][n-1])