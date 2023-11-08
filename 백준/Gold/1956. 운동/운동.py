import sys

input = sys.stdin.readline
INF = int(1e9)
result = INF

v, e = map(int,input().split())
graph = [[INF for _ in range(v+1)] for _ in range(v+1)]

for i in range(e):
  start, end, cost = map(int,input().split())
  graph[start][end] = cost

for k in range(1,v+1):
  for i in range(1,v+1):
    for j in range(1,v+1):
      graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

for k in range(1,v+1):
  result = min(result,graph[k][k])

if result == INF:
  print(-1)
else:
  print(result)