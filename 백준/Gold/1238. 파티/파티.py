import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
result = 0

def dijkstra(a):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q,(0,a))
  distance[a] = 0

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

n, m, x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  start, end, length = map(int,input().split())
  graph[start].append((end,length))

for i in range(1,n+1):
  go_length = dijkstra(i)[x]
  back_length = dijkstra(x)[i]

  result = max(result, go_length + back_length)

print(result)