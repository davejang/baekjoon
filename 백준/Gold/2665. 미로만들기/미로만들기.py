import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
arr = []
visited = [[0 for _ in range(n)] for _ in range(n)]
count = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
  arr.append(list(str(input().rstrip())))

q = deque()
q.append((0,0))
visited[0][0] = 1
count[0][0] = 0

while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
      if arr[nx][ny] == '0':
        q.append((nx,ny))
        count[nx][ny] = min(count[x][y] + 1, count[nx][ny])
      if arr[nx][ny] == '1':
        count[nx][ny] = min(count[x][y], count[nx][ny])
        q.appendleft((nx,ny))

      visited[nx][ny] = 1
      
print(count[-1][-1])