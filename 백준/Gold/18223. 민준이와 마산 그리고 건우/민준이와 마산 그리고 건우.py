import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(x):
  q = []
  distance = [INF] * (v+1)

  heapq.heappush(q,(0,x))
  distance[x] = 0

  while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
      continue

    for next in graph[now]:
      cost = dist + next[1]
      if cost < distance[next[0]]:
        distance[next[0]] = cost
        heapq.heappush(q,(cost,next[0]))
        
  return distance

v, e, p = map(int,input().split())
graph = [[] for _ in range(v+1)]

for i in range(e):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

if dijkstra(1)[p] + dijkstra(p)[v] == dijkstra(1)[v]:
  print("SAVE HIM")
else:
  print("GOOD BYE")