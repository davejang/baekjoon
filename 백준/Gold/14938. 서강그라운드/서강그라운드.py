import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
max_result = 0

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q:
    cur_cost, node = heapq.heappop(q)

    if distance[node] < cur_cost:
      continue

    for n in graph[node]:
      cost = cur_cost + n[1]
      if cost < distance[n[0]]:
        distance[n[0]] = cost
        heapq.heappush(q,(cost,n[0]))

  return distance

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
item = [0]
item = item + list(map(int,input().rstrip().split()))

for i in range(r):
  start, end, cost = map(int,input().split())
  graph[start].append((end,cost))
  graph[end].append((start,cost))

for i in range(1,n+1):
  distance = [INF] * (n+1)
  d = dijkstra(i)
  temp = 0
  for j in range(1,n+1):
    if m >= d[j]:
      temp += item[j]

  max_result = max(max_result,temp)

print(max_result)