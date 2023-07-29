import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for i in range(n-1):
  start, end = map(int,input().split())
  graph[start].append(end)
  graph[end].append(start)

def bfs(a):
  q = deque([])
  q.append(a)

  while q:
    x = q.popleft()
    for i in graph[x]:
      if parent[i] == 0:
        parent[i] = x
        q.append(i)
  
bfs(1)
for i in range(2,n+1):
  print(parent[i])