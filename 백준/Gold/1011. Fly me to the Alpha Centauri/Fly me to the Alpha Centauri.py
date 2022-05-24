import math

testcase = int(input())
x_list = []
y_list = []
length = []

for i in range(testcase):
  x, y = map(int,input().split())
  x_list.append(x)
  y_list.append(y)
  length.append(y-x)

for i in range(testcase):
  if int(math.sqrt(length[i]))**2 == length[i]:
    print(int(math.sqrt(length[i]))*2-1)
  elif length[i] <= int(math.sqrt(length[i]))**2 + int(math.sqrt(length[i])):
    print(int(math.sqrt(length[i]))*2)
  else:
    print(int(math.sqrt(length[i]))*2+1)