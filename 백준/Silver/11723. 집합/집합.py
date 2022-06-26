import sys
input = sys.stdin.readline
n = int(input())
set = [0]*21
for i in range(n):
  call = list(str(input()).split())
  if len(call) == 2:
    call[1] = int(call[1])
  if call[0] == 'add':
    if set[call[1]] == 1:
      continue
    else:
      set[call[1]] = 1
  elif call[0] == 'remove':
    if set[call[1]] == 1:
      set[call[1]] = 0
  elif call[0] == 'check':
    if set[call[1]] == 1:
      print(1)
    else:
      print(0)
  elif call[0] == 'toggle':
    if set[call[1]] == 1:
      set[call[1]] = 0
    else:
      set[call[1]] = 1
  elif call[0] == 'all':
    set = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
  elif call[0] == 'empty':
    set = [0]*21
      