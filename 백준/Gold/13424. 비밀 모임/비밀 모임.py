import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline

def dijkstra(x):
  distance = [INF] * (n+1)
  
  q = []
  distance[x] = 0
  heapq.heappush(q,(0,x))

  while q:
    dist, cur = heapq.heappop(q)
    
    if distance[cur] < dist:
      continue

    for next in graph[cur]:
      cost = dist + next[1]
      if cost < distance[next[0]]:
        distance[next[0]] = cost
        heapq.heappush(q,(cost,next[0]))

  return distance

t = int(input())

for i in range(t):
  n, m = map(int,input().split())
  graph = [[] for _ in range(n+1)]
  
  for j in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

  k = int(input())
  friend = list(map(int,input().rstrip().split()))

  cnt = [0] * (n+1)
  cnt[0] = INF
  for idx in friend:
    temp = dijkstra(idx)
    for l in range(1,n+1):
      cnt[l] += temp[l]

  print(cnt.index(min(cnt)))