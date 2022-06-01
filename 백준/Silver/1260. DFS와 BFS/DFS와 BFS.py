from collections import deque

N, M, V = map(int,input().split())
graph = {}
stack = [0]*(N+1)
queue = [0]*(N+1)
visited = [0]*(N+1)

for i in range(N):
  graph[i+1] = []

for i in range(M):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N):
  graph[i+1].sort()

def dfs(v):
  stack[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not stack[i]:
      dfs(i)
def bfs(v):
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
dfs(V)
print("")
bfs(V)