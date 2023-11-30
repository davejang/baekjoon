import sys
import heapq

input = sys.stdin.readline
INF = int(1e12)

n, m = map(int,input().split())
graph = [[] for _ in range(n)]
distance = [INF] * (n)
sight = list(map(int,input().rstrip().split()))

for i in range(m):
  start, end, cost = map(int,input().split())
  graph[start].append((cost,end))
  graph[end].append((cost,start))

def dijkstra(node):
  q = []
  heapq.heappush(q,(0,node))
  distance[node] = 0

  while q:
    cur_cost, cur_node = heapq.heappop(q)

    if distance[cur_node] < cur_cost:
      continue

    for next_cost, next_node in graph[cur_node]:
      if sight[next_node] == 1 and next_node != n-1:
        continue
        
      cost = cur_cost + next_cost

      if distance[next_node] > cost:
        distance[next_node] = cost
        heapq.heappush(q,(cost,next_node))

  return distance[-1]

result = dijkstra(0)
if result == INF:
  print(-1)
else:
  print(result)