import sys

input = sys.stdin.readline

min_result = int(1e9)

graph = []
n = int(input())
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))
visited = [0 for _ in range(n)]

def dfs(depth,idx):
  global min_result
  if depth == n//2:
    a_team = 0
    b_team = 0
    for i in range(n):
      for j in range(n):
        if visited[i] == 1 and visited[j] == 1:
          a_team += graph[i][j]
        elif visited[i] == 0 and visited[j] == 0:
          b_team += graph[i][j]

    min_result = min(min_result,abs(a_team-b_team))
    return

  for i in range(idx,n):
    if visited[i] == 0:
      visited[i] = 1
      dfs(depth+1,i+1)
      visited[i] = 0
    
dfs(0,0)
print(min_result)