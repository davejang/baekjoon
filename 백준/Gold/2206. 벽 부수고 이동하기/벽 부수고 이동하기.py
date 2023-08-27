import sys
from collections import deque

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,z):
  q = deque([])
  q.append((x,y,z))
  visited[x][y][z] = 1

  while q:
    a, b, c = q.popleft()
    if a == n -1 and b == m - 1:
      return visited[a][b][c]
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if arr[nx][ny] == 1 and c == 0:
        visited[nx][ny][1] = visited[a][b][c] + 1
        q.append((nx,ny,1))

      if arr[nx][ny] == 0 and visited[nx][ny][c] == 0:
        visited[nx][ny][c] = visited[a][b][c] + 1
        q.append((nx,ny,c))

  return -1
  
n, m = map(int,input().split())
arr = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

for i in range(n):
  arr.append(list(map(int,list(input().rstrip()))))

print(bfs(0,0,0))