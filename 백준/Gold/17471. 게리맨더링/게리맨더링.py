import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
INF = int(1e9)

def bfs(group):
  p = 0
  visited = set([])
  q = deque()
  
  q.append(group[0])
  visited.add(group[0])
  p += population[group[0]]

  while q:
    cur = q.popleft()
    for next in graph[cur]:
      if next not in visited and next in group:
        q.append(next)
        visited.add(next)
        p += population[next]

  return p

def dfs(count,group):
  global n
  global min_result
  
  if count == n-1:
    return

  v1 = bfs(group)
  v2 = bfs([i for i in range(1,n+1) if i not in group])
  
  if v1 + v2 == sum(population):
    min_result = min(min_result,abs(v1-v2))

  for next in graph[group[-1]]:
    if next not in group:
      group.append(next)
      dfs(count+1,group.copy())
      group.pop()

min_result = INF
n = int(input())
graph = [[] for _ in range(n+1)]
population = [0] * (n+1)

pop = list(map(int,input().rstrip().split()))
for i in range(n):
  population[i+1] = pop[i]

for i in range(1,n+1):
  node_list = list(map(int,input().rstrip().split()))
  for j in range(1,len(node_list)):
    graph[i].append(node_list[j])

# for i in range(1,n//2+1):
#   start = []
#   start.append(i)
#   dfs(0,start)

for i in range(1, n//2+1):
  comb = tuple(combinations([a for a in range(1,n+1)], i))
  for A in comb:
    B = [i for i in range(1,n+1) if i not in A]

    v1 = bfs(A)
    v2 = bfs(B)
    if v1 + v2 == sum(population):
      min_result = min(min_result,abs(v1-v2))

if min_result == INF:
  print(-1)
else:
  print(min_result)