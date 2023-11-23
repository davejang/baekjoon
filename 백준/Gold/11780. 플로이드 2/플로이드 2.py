import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
nav = [[[] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0

for i in range(m):
  start, end, cost = map(int,input().split())
  graph[start][end] = min(graph[start][end],cost)

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if graph[i][k] + graph[k][j] < graph[i][j]:
        graph[i][j] = graph[i][k] + graph[k][j]
        nav[i][j] = nav[i][k] + [k] + nav[k][j]

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == INF:
      print(0, end = ' ')
    else:
      print(graph[i][j], end = ' ')
  print()

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == INF or graph[i][j] == 0:
      print(0, end = ' ')
    else:
      print(len(nav[i][j])+2, end = ' ')
      print(i, end = ' ')
      for c in nav[i][j]:
        print(c, end = ' ')
      print(j, end = ' ')
      
    print()