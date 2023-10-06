import sys
from collections import deque

input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]
graph = []
queue = []
num = 0
dict = {}
count = 0

n, k = map(int,input().split())
chess_info = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))
for i in range(k):
  num += 1
  r, c, dir = map(int,input().split())
  chess_info[r-1][c-1].append(num)
  dict[num] = [r-1,c-1,dir-1]

def move(i,r,c):
  dir = dict[i][2]
  # stack_move : 이동할 스택
  # stack : 남아있는 스택
  stack_move = deque(chess_info[r][c])
  stack = []
  while stack_move:
    horse = stack_move.popleft()
    if horse == i:
      stack_move.appendleft(i)
      break
    stack.append(horse)
  stack_move = list(stack_move)

  # 이동할 방향
  nr = r + dx[dir]
  nc = c + dy[dir]
  # 범위 안에 있는 경우
  if 0 <= nr < n and 0 <= nc < n:
    # 흰색/빨간색
    if graph[nr][nc] == 0 or graph[nr][nc] == 1:
      # 이동하는 스택 위치 갱신
      for horse in stack_move:
        dict[horse][0] = nr
        dict[horse][1] = nc
      if graph[nr][nc] == 1:
        stack_move.reverse()
      chess_info[nr][nc] += stack_move
      chess_info[r][c] = stack
      if len(chess_info[nr][nc]) >= 4:
        return True

    # 파란색
    if graph[nr][nc] == 2:
      if dir == 1 or dir == 3:
        dir -= 1
      else:
        dir += 1
      dict[i][2] = dir
      nr = r + dx[dir]
      nc = c + dy[dir]
      if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] < 2:
        # 이동하는 스택 위치 갱신
        for horse in stack_move:
          dict[horse][0] = nr
          dict[horse][1] = nc
        if graph[nr][nc] == 1:
          stack_move.reverse()
        chess_info[nr][nc] += stack_move
        chess_info[r][c] = stack
        if len(chess_info[nr][nc]) >= 4:
          return True
  # 범위 밖에 있는 경우
  else:
    if dir == 1 or dir == 3:
      dir -= 1
    else:
      dir += 1
    dict[i][2] = dir
    nr = r + dx[dir]
    nc = c + dy[dir]
    if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] < 2:
      # 이동하는 스택 위치 갱신
      for horse in stack_move:
        dict[horse][0] = nr
        dict[horse][1] = nc
      if graph[nr][nc] == 1:
        stack_move.reverse()
      chess_info[nr][nc] += stack_move
      chess_info[r][c] = stack
      if len(chess_info[nr][nc]) >= 4:
        return True

  return False

flag = False
while True:
  if count > 1000:
    count = -1
    break
  count += 1
  for i in range(1,k+1):
    r, c, dir = dict[i]
    flag = move(i,r,c)
    if flag:
      break
  if flag:
    break

print(count)