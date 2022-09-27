n, m = map(int,input().split())
array = []
cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
for i in range(n):
  array.append(list(map(int,input().split())))
  
for i in range(m):
  move_cloud = []
  d, s = map(int,input().split())
  for i in cloud:
    x = i[0]
    y = i[1]
    nx = (n + x + dx[d-1] * s) % n
    ny = (n + y + dy[d-1] * s) % n
    move_cloud.append((nx,ny))
    array[nx][ny] += 1

  for i in move_cloud:
    count = 0
    x = i[0]
    y = i[1]
    for i in range(1,9,2):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if array[nx][ny] > 0:
        count += 1
    array[x][y] += count

  cloud = []
  for r in range(n):
    for c in range(n):
      if array[r][c] >= 2:
        if (r,c) in move_cloud:
          continue
        array[r][c] -= 2
        cloud.append((r,c))

answer = 0
for r in range(n):
  for c in range(n):
      answer += array[r][c]
print(answer)