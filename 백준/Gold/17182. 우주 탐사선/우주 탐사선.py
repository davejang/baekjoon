import sys

input = sys.stdin.readline
INF = int(1e9)

n, K = map(int,input().split())
graph = []
result = INF
visited = [False] * n
visited[K] = True

def track(start,count,dist):
  global result

  if count == n:
    result = min(result,dist)
    return

  for next in range(n):
    if visited[next] == False:
      visited[next] = True
      track(next, count + 1, dist + graph[start][next])
      visited[next] = False

for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

track(K,1,0)

print(result)