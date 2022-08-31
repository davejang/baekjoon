import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
visited = [False]*(N+1)
count = 0

for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  queue = deque([])
  queue.append(v)
  visited[v] = True
  while queue:
    n = queue.popleft()
    for i in graph[n]:
      if visited[i] == False:
        visited[i] = True
        queue.append(i)

for i in range(1,N+1):
  if visited[i] == False:
    if not graph[i]:
      count += 1
      visited[i] = True
    else:
      bfs(i)
      count += 1

print(count)