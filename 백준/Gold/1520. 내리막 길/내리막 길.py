import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(a,b):
  if a == n - 1 and b == m - 1:
    return 1
  if visited[a][b] == -1:
    visited[a][b] = 0
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
        
      if arr[nx][ny] < arr[a][b]:
        visited[a][b] += dfs(nx,ny)

  return visited[a][b]
      
n, m = map(int,input().split())
arr = []
visited = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
  arr.append(list(map(int,input().split())))

print(dfs(0,0))