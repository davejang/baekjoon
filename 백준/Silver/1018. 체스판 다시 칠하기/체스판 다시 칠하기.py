n, m = map(int,input().split())
chess = []
refill = 64
for i in range(n):
  array = list(str(input().strip()))
  chess.append(array)

for i in range(n-7):
  for j in range(m-7):
    count_1 = 0
    count_2 = 0
    for x1 in range(8):
      for y1 in range(8):
        if (x1 + y1) % 2 == 1:
          if chess[x1+i][y1+j] == 'B':
            count_1 = count_1 + 1
        else:
          if chess[x1+i][y1+j] == 'W':
            count_1 = count_1 + 1
    for x2 in range(8):
      for y2 in range(8):
        if (x2 + y2) % 2 == 1:
          if chess[x2+i][y2+j] == 'W':
            count_2 = count_2 + 1
        else:
          if chess[x2+i][y2+j] == 'B':
            count_2 = count_2 + 1
    refill = min(refill,count_1,count_2)
print(refill)