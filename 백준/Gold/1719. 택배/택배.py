import sys

input = sys.stdin.readline
INF = int(1e9)


n, m = map(int,input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
last = [['-' for _ in range(n+1)] for _ in range(n+1)]
result = [['-' for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
  for j in range(n+1):
    if i == j:
      graph[i][j] = 0

for i in range(m):
  start, end, cost = map(int,input().split())
  graph[start][end] = cost
  last[start][end] = end
  graph[end][start] = cost
  last[end][start] = start

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if graph[i][j] > graph[i][k] + graph[k][j]:
        graph[i][j] = graph[i][k] + graph[k][j]
        last[i][j] = k

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      print('-',end = " ")
      continue
    temp = last[i][j]
    while True:
      if temp == last[i][temp]:
        break
      temp = last[i][temp]
    print(temp,end = " ")
    result[i][j] = temp
  print()