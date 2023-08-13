import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
result = 0

def dijkstra(start, end):
  q = []
  distance = [INF] * (n+1)
  heapq.heappush(q,((0,start)))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue 
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

  return distance[end]

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
  start, end, length = map(int,input().split())
  graph[start].append((end,length))
  graph[end].append((start,length))

v1, v2 = map(int,input().split())

result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n))
if result >= INF:
  print(-1)
else:
  print(result)
