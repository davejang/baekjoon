from collections import deque

n = int(input())
array = [[0 for col in range(n)] for row in range(n)]
queue = deque([])
snake_queue = deque([])
array[0][0] = -1 # -1 : snake / 0 : none / 1 : apple
current_d = 1 # 1 : right / 2 : down / 3 : left / 4 : up
second = 0
a = 0
b = 0
snake_queue.append((a,b))

k = int(input())
for i in range(k):
  x, y = map(int,input().split())
  array[x-1][y-1] = 1
  
l = int(input())
for j in range(l):
  sec, loc = map(str,input().split())
  sec = int(sec)
  queue.append((sec,loc))

while True:
  second += 1
  
  if current_d == 1: # right
    if b + 1 >= n:
      break
    if array[a][b+1] == 1:
      array[a][b+1] = -1
      snake_queue.append((a,b))
    else:
      snake_queue.append((a,b))
      tail_x, tail_y = snake_queue.popleft()
      array[tail_x][tail_y] = 0
      if array[a][b+1] == -1:
        break
      array[a][b+1] = -1
    b = b + 1
  
  elif current_d == 2: # down
    if a + 1 >= n:
      break
    if array[a+1][b] == 1:
      snake_queue.append((a,b))
      array[a+1][b] = -1
    else:
      snake_queue.append((a,b))
      tail_x, tail_y = snake_queue.popleft()
      array[tail_x][tail_y] = 0
      if array[a+1][b] == -1:
        break
      array[a+1][b] = -1
    a = a + 1
  
  elif current_d == 3: # left
    if b - 1 < 0:
      break
    if array[a][b-1] == 1:
      snake_queue.append((a,b))
      array[a][b-1] = -1
    else:
      snake_queue.append((a,b))
      tail_x, tail_y = snake_queue.popleft()
      array[tail_x][tail_y] = 0
      if array[a][b-1] == -1:
        break
      array[a][b-1] = -1
    b = b - 1
  
  elif current_d == 4: # up
    if a - 1 < 0:
      break
    if array[a-1][b] == 1:
      snake_queue.append((a,b))
      array[a-1][b] = -1
    else:
      snake_queue.append((a,b))
      tail_x, tail_y = snake_queue.popleft()
      array[tail_x][tail_y] = 0
      if array[a-1][b] == -1:
        break
      array[a-1][b] = -1
    a = a - 1
    
  if queue:
    if queue[0][0] == second:
      change = queue.popleft()
      if change[1] == 'D':
        current_d = current_d + 1
        if current_d == 5:
          current_d = 1
      elif change[1] == 'L':
        current_d = current_d - 1
        if current_d == 0:
          current_d = 4

print(second)