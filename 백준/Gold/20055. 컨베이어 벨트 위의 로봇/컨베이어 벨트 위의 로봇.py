import sys
from collections import deque

input = sys.stdin.readline

top = deque([])
bottom = deque([])
n, k = map(int,input().split())
durability = list(map(int,input().split()))
robot_info = deque([0] * n)
count = 0
result = 0

for i in range(n):
  top.append(durability[i])

for i in range(n):
  bottom.appendleft(durability[n + i])

while True:

  # 1
  a = top.pop()
  b = bottom.popleft()
  top.appendleft(b)
  bottom.append(a)
  robot_info.appendleft(0)
  robot_info.pop()
  robot_info[-1] = 0

  # 2
  for j in range(n-2,0,-1):
    if robot_info[j] == 1 and robot_info[j+1] == 0 and top[j+1] > 0:
      robot_info[j] = 0
      robot_info[j+1] = 1
      top[j+1] -= 1

  # 3
  if top[0] > 0 and robot_info[0] == 0:
    robot_info[0] = 1
    top[0] -= 1

  # 4
  top_count = list(top).count(0)
  bottom_count = list(bottom).count(0)
  count = top_count + bottom_count

  result += 1
  if count >= k:
    print(result)
    break