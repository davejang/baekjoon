import sys

input = sys.stdin.readline
graph = []
sand = 0
legth = 0
cur_dir = 0
cur_len = 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 방향 별 모래 분포 (마지막 비율 0일 경우 a에 해당)
left = [(1,1,0.01),(-1,1,0.01),(1,0,0.07),(-1,0,0.07),(1,-1,0.10),(-1,-1,0.10),
   (0,-2,0.05),(2,0,0.02),(-2,0,0.02),(0,-1,0)]
down = [(-y,x,z) for x,y,z in left]
right = [(x,-y,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]
dict = {0: left, 1: down, 2: right, 3: up}

n = int(input())
x, y = n // 2, n // 2
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

# 모래 계산
def sand_move(x,y,dir):
  global sand

  if y < 0:
    return

  a = 0
  for dx, dy, z in dir:
    nx = x + dx
    ny = y + dy
    if z > 0:
      temp_sand = int(graph[x][y] * z)
      a += temp_sand
    else:
      temp_sand = graph[x][y] - a

    if 0 <= nx < n and 0 <= ny < n:
      graph[nx][ny] += temp_sand
    # 범위 넘어갈 경우
    else:
      sand += temp_sand

while True:
  if y < 0:
    break
  if cur_dir == 0 or cur_dir == 2:
    legth += 1
  for i in range(legth):
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    sand_move(nx,ny,dict[cur_dir])
    x, y = nx, ny
  cur_dir = (cur_dir + 1) % 4

print(sand)