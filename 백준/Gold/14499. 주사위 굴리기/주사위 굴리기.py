from collections import deque

n, m, y, x, k = map(int,input().split())
array = []
dice = [0,0,0,0,0,0] # bottom, top, x_right, x_left, y_up, y_down

for i in range(n):
  array.append(list(map(int,input().split())))
command = list(map(int,input().split()))
queue = deque(command)

for j in range(k):
  current_command = queue.popleft()

  if current_command == 1:
    if x + 1 >= m:
        continue
    x = x + 1
    temp = [dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]]
    dice[0] = temp[2]
    dice[1] = temp[3]
    dice[2] = temp[1]
    dice[3] = temp[0]
    if array[y][x] == 0:
      array[y][x] = dice[0]
      print(dice[1])
    else:
      dice[0] = array[y][x]
      array[y][x] = 0
      print(dice[1])
      
  elif current_command == 2:
    if x - 1 < 0:
        continue
    x = x - 1
    temp = [dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]]
    dice[0] = temp[3]
    dice[1] = temp[2]
    dice[2] = temp[0]
    dice[3] = temp[1]
    if array[y][x] == 0:
      array[y][x] = dice[0]
      print(dice[1])
    else:
      dice[0] = array[y][x]
      array[y][x] = 0
      print(dice[1])

  elif current_command == 3:
    if y - 1 < 0:
        continue
    y = y - 1
    temp = [dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]]
    dice[0] = temp[4]
    dice[1] = temp[5]
    dice[4] = temp[1]
    dice[5] = temp[0]
    if array[y][x] == 0:
      array[y][x] = dice[0]
      print(dice[1])
    else:
      dice[0] = array[y][x]
      array[y][x] = 0
      print(dice[1])

  elif current_command == 4:
    if y + 1 >= n:
        continue
    y = y + 1
    temp = [dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]]
    dice[0] = temp[5]
    dice[1] = temp[4]
    dice[4] = temp[0]
    dice[5] = temp[1]
    if array[y][x] == 0:
      array[y][x] = dice[0]
      print(dice[1])
    else:
      dice[0] = array[y][x]
      array[y][x] = 0
      print(dice[1])