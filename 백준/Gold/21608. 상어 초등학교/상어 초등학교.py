n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
array = [[0 for col in range(n)] for row in range(n)]
student_info = []
answer = 0

def fav_search(x,y,fav_student):
  fav_near = 0
  near_null = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue
    if array[nx][ny] in fav_student:
      fav_near += 1
    if array[nx][ny] == 0:
      near_null += 1
  return fav_near, near_null

for i in range(n*n):
  fav_info = list(map(int,input().split()))
  current_student = fav_info[0]
  fav_student = fav_info[1:]
  candidate_seat = []
  fav_near_max = 0
  
  for r in range(n):
    for c in range(n):
      if array[r][c] != 0:
        continue
      fav_count, null_count = fav_search(r,c,fav_student)
      candidate_seat.append([fav_count,null_count,r,c])
  candidate_seat.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
  array[candidate_seat[0][2]][candidate_seat[0][3]] = current_student
  student_info.append([fav_info,candidate_seat[0][2],candidate_seat[0][3]])

for info in student_info:
  current_student = info[0][0]
  fav_list = info[0][1:]
  x = info[1]
  y = info[2]
  fav_near = 0
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue
    if array[nx][ny] in fav_list:
      fav_near += 1
      
  if fav_near == 0:
    answer += 0
  elif fav_near == 1:
    answer += 1
  elif fav_near == 2:
    answer += 10
  elif fav_near == 3:
    answer += 100
  else:
    answer += 1000

print(answer)