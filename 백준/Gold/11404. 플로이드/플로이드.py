import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
  for j in range(n+1):
    if i == j:
      graph[i][j] = 0

for i in range(m):
  start, end, cost = map(int,input().split())
  graph[start][end] = min(cost,graph[start][end])

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == INF:
      print("0",end = " ")
    else:
      print(graph[i][j],end = " ")
  print()