from collections import deque

n, k = map(int,input().split())
graph = {}
visited = [0]*(200001)
dp = [-1,1,0]
dx = [0,0,1]

queue = deque([])
queue.append(n)
while queue:
  v = queue.popleft()
  if v == k:
    break
  for i in range(3):
    dv = v + dp[i] + v*dx[i]
    if(dv>=200000) or dv<0:
      continue
    if visited[dv] == 0:
      visited[dv] = visited[v] + 1
      queue.append(dv)
print(visited[k])