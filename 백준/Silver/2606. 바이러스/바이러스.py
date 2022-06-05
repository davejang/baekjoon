import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
graph = {}
visited = [0]*(n+1)
infected_list = []
for i in range(n):
  graph[i+1] = []
for i in range(k):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

queue = deque([])
queue.append(1)
while queue:
  v = queue.popleft()
  for i in graph[v]:
    if visited[i] == 0:
      visited[i] = 1
      infected_list.append(i)
      queue.append(i)
print(len(infected_list)-1)