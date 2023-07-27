import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
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
      
n, k = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(100001)]
distance = [INF] * 100001

for i in range(100001):
  if i < 100000:
    graph[i].append((i+1,1))
  if i > 0:
    graph[i].append((i-1,1))
  if i * 2 < 100001:
    graph[i].append((i*2,0))

dijkstra(n)
print(distance[k])