import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  distance = [INF] * (v+1)
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
  
  return distance

v, e = map(int,input().split())
graph = [[] for _ in range(v+1)]
s = int(input())
for i in range(e):
  start, end, length = map(int,input().split())
  graph[start].append((end,length))
result = dijkstra(s)

for i in range(1,len(result)):
  if result[i] == INF:
    print('INF')
  else:
    print(result[i])