import math
t = int(input())

def calculate(x1,y1,r1,x2,y2,r2):
  turret_distance = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
  if turret_distance == 0 and r1 == r2:
    return -1
  elif r1 + r2 == turret_distance or abs(r1 - r2) == turret_distance:
    return 1
  elif abs(r1 - r2) < turret_distance < r1 + r2:
    return 2
  else:
    return 0
  
for i in range(t):
  x1,y1,r1,x2,y2,r2 = map(int,input().split())
  print(calculate(x1,y1,r1,x2,y2,r2))