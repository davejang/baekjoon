import sys
input = sys.stdin.readline

r, c, t = map(int,input().split())
array = []
for i in range(r):
  array.append(list(map(int,input().split())))
air_position = []
for i in range(r):
  if array[i][0] == -1:
    air_position.append((i,0))

def dust():
  temp = [[0 for col in range(c)] for row in range(r)]
  for x in range(r):
    for y in range(c):
      if array[x][y] >= 5:
        count = 0
        if x - 1 >= 0 and array[x-1][y] != -1:
          temp[x-1][y] += int(array[x][y]/5)
          count += 1
        if x + 1 < r and array[x+1][y] != -1:
          temp[x+1][y] += int(array[x][y]/5)
          count += 1
        if y - 1 >= 0 and array[x][y-1] != -1:
          temp[x][y-1] += int(array[x][y]/5)
          count += 1
        if y + 1 < c and array[x][y+1] != -1:
          temp[x][y+1] += int(array[x][y]/5)
          count += 1
        temp[x][y] -= (int(array[x][y]/5)) * count
  for x in range(r):
    for y in range(c):
      array[x][y] += temp[x][y]

def air_top():
  dx = [0,-1,0,1]
  dy = [1,0,-1,0]
  x, y = air_position[0][0], 1
  d = 0
  temp = 0

  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if x == air_position[0][0] and y == air_position[0][1]:
      break
    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      d+=1
      continue
    array[x][y], temp = temp, array[x][y]
    x, y = nx, ny

    
def air_bottom():
  dx = [0,1,0,-1]
  dy = [1,0,-1,0]
  x, y = air_position[1][0], 1
  d = 0
  temp = 0

  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if x == air_position[1][0] and y == air_position[0][1]:
      break
    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      d+=1
      continue
    array[x][y], temp = temp, array[x][y]
    x, y = nx, ny

for i in range(t):
  dust()
  air_top()
  air_bottom()

sum = 0
for a in range(r):
  for b in range(c):
    sum += array[a][b]
print(sum+2)