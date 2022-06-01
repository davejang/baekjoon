from collections import deque

N, M, V = map(int,input().split())
graph = {}
visited1 = [0]*(N+1)
visited2 = [0]*(N+1)

for i in range(N):
  graph[i+1] = []

for i in range(M):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N):
  graph[i+1].sort()

def dfs(v):
  visited1[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited1[i]:
      dfs(i)
def bfs(v):
  queue = deque([])
  visited2[v] = True
  print(v,end=' ')
  while (0 in visited2) == True:
    for i in graph[v]:
      if not visited2[i]:
        visited2[i] = True
        queue.append(i)
        print(i,end=' ')
    if(len(queue) == 0):
      break
    v = queue.popleft()

dfs(V)
print("")
bfs(V)