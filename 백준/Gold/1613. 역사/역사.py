import sys

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int,input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
result = []

for i in range(k):
  start, end = map(int,input().split())
  graph[start][end] = 1

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

s = int(input())

for i in range(s):
  start, end = map(int,input().split())
  if graph[start][end] == INF and graph[end][start] == INF:
    result.append(0)
  elif graph[start][end] == INF and graph[end][start] != INF:
    result.append(1)
  elif graph[start][end] != INF and graph[end][start] == INF:
    result.append(-1)

for i in result:
  print(i)