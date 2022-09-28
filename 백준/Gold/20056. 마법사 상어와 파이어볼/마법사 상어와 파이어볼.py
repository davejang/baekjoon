n, m , k = map(int,input().split())
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
array = [[[0,0,0,0,0] for col in range(n)] for row in range(n)]
fireballs = []
answer = 0

for i in range(m):
  fireball = list(map(int,input().split()))
  fireballs.append(fireball)
  fireball[0] -= 1
  fireball[1] -= 1

for i in range(k):
  for fireball in fireballs:
    fireball[0] = (fireball[0] + dx[fireball[4]] * fireball[3]) % n
    fireball[1] = (fireball[1] + dy[fireball[4]] * fireball[3]) % n
    
    array[fireball[0]][fireball[1]][0] += fireball[2]
    array[fireball[0]][fireball[1]][1] += fireball[3]
    array[fireball[0]][fireball[1]][2] += 1
    array[fireball[0]][fireball[1]][3] = fireball[4]
    
    if array[fireball[0]][fireball[1]][4] == 0:
      if fireball[4] % 2 == 1:
        array[fireball[0]][fireball[1]][4] = 1
      else:
        array[fireball[0]][fireball[1]][4] = 2
    elif array[fireball[0]][fireball[1]][4] == 1:
      if fireball[4] % 2 == 1:
        array[fireball[0]][fireball[1]][4] = 1
      else:
        array[fireball[0]][fireball[1]][4] = 3
    elif array[fireball[0]][fireball[1]][4] == 2:
      if fireball[4] % 2 == 1:
        array[fireball[0]][fireball[1]][4] = 3
      else:
        array[fireball[0]][fireball[1]][4] = 2
    
  fireballs  = []
  answer = 0

  for r in range(n):
    for c in range(n):
      if array[r][c][2] >= 2:
        m = array[r][c][0] // 5
        if m == 0:
          array[r][c] = [0,0,0,0,0]
          continue
        s = array[r][c][1] // array[r][c][2]
        if array[r][c][4] == 1 or array[r][c][4] == 2:
          for d in range(0,8,2):
            fireballs.append([r,c,m,s,d])
        else:
          for d in range(1,8,2):
            fireballs.append([r,c,m,s,d])
        array[r][c] = [0,0,0,0,0]
        answer += 4 * m
      if array[r][c][2] == 1:
        m = array[r][c][0]
        s = array[r][c][1]
        d = array[r][c][3]
        answer += m
        fireballs.append([r,c,m,s,d])
        array[r][c] = [0,0,0,0,0]
        
print(answer)