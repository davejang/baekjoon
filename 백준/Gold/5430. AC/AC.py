from collections import deque

T = int(input())
result = []
for i in range(T):
  checkTrue = True
  checkReverse = 0
  p = str(input())
  n = int(input())
  if n == 0:
    array = input()
    array = []
  else:
    array = deque(map(int, input()[1:-1].split(',')))
  
  for j in range(len(p)):
    if p[j] == "R":
      checkReverse = checkReverse + 1
    if p[j] == "D":
      if len(array) == 0:
        checkTrue = False
      else:
        if checkReverse % 2 == 0:
          array.popleft()
        else:
          array.pop()
  if checkReverse % 2 == 1:
    array.reverse()

  if checkTrue == True:
    result.append(array)
  else:
    result.append('error')

for i in result:
  if i == 'error':
    print(i)
  else:
    print('[' + ','.join([str(x) for x in i]) + ']')