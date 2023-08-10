import sys

input = sys.stdin.readline

def dfs(u, visited):
    visited.add(u)
    for node in graph[u]:
        if node not in visited:
            dfs(node, visited.copy())
        else: 
            result.extend(list(visited))
            return
      
n = int(input())
result = []
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
  graph[int(input())].append(i)

for i in range(1,n+1):
  dfs(i,set([]))

result = list(set(result))
result.sort()
print(len(result))
for i in result:
  print(i)