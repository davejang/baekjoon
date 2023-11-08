import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(n):
  q = []
  heapq.heappush(q,(0,n))
  distance[n] = 0

  while q:
    cost, cur = heapq.heappop(q)

    if distance[cur] < cost:
      continue

    for dis, node in graph[cur]:
      new_cost = cost + dis
      if distance[node] > new_cost:
        distance[node] = new_cost
        heapq.heappush(q,(new_cost,node))

  return distance

t = int(input())
for i in range(t):
  count = 0
  time = 0
  n, d, c = map(int,input().split())
  graph = [[] for _ in range(n+1)]
  distance = [INF] * (n+1)
  
  for i in range(d):
    a, b, s = map(int,input().split())
    graph[b].append((s,a))

  dis = dijkstra(c)
  
  for i in dis:
    if i != INF:
      count += 1
      time = max(time,i)

  print(count,time)