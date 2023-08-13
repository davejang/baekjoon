import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start,end):
  q = []
  distance = [INF] * (n+1)
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

  return distance[end]

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
  start, end, cost = map(int,input().split())
  graph[start].append((end,cost))

a, b = map(int,input().split())
print(dijkstra(a,b))