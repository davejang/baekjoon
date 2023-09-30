import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
# 결과
result_eat = 0
graph = [[None]*4 for _ in range(4)]

for i in range(4):
    data=list(map(int, input().split()))
    for j in range(4):
        graph[i][j]=[data[j*2],data[j*2+1]-1]

# 물고기의 위치와 방향을 반환
def find_fish(graph,n):
  for i in range(4):
    for j in range(4):
      if graph[i][j][0] == n:
        return i, j

  return False

def fish_move(graph,shark_x,shark_y):
  for i in range(1,17):
    position = find_fish(graph,i)
    if position != False:
      x, y = position
      direction = graph[x][y][1]
      for j in range(8):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0<= nx <4 and 0 <= ny <4:
          if not (nx == shark_x and ny == shark_y):
            graph[x][y][1] = direction
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            break
        direction = (direction+1) % 8

def check_moveable(graph,x,y):
  move_list = []
  dir = graph[x][y][1]

  for i in range(4):
    x += dx[dir]
    y += dy[dir]

    if x < 0 or y < 0 or x >= 4 or y >= 4:
      continue
    if graph[x][y][0] == 0:
      continue

    move_list.append((x,y))

  return move_list
  
def shark_move(graph,x,y,eat):
  global result_eat
  graph = copy.deepcopy(graph)
  
  eat += graph[x][y][0]
  graph[x][y] = (0,graph[x][y][1])
  fish_move(graph,x,y)

  shark_moveable_list = check_moveable(graph,x,y)

  if not shark_moveable_list:
    result_eat = max(eat,result_eat)
    return

  for nx, ny in shark_moveable_list:
    shark_move(graph,nx,ny,eat)

shark_move(graph,0,0,0)
print(result_eat)