import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
result = []

def dijkstra(s,e):
  q = []
  heapq.heappush(q,(0,s))
  distance[s] = 0

  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue

    for node in graph[now]:
      cost = dist + node[0]
      if cost < distance[node[1]]:
        distance[node[1]] = cost
        last[node[1]] = now
        heapq.heappush(q,(cost,node[1]))

  print(distance[e])
  
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
last = [INF] * (n+1)

for i in range(m):
  start, end, cost = map(int,input().split())
  graph[start].append((cost,end))

s, e = map(int,input().split())
dijkstra(s,e)
result.append(e)
temp = e

while True:
  if last[temp] == INF:
    break
  else:
    result.append(last[temp])
    temp = last[temp]

result.reverse()

print(len(result))
for i in result:
  print(i,end = " ")