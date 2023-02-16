import sys
from collections import deque

input = sys.stdin.readline
time = 0

n, w, l = map(int,input().split())
truck_w = deque(list(map(int,input().split())))

bridge_queue = deque([0] * w)

while True:
  time += 1
  bridge_queue.popleft()

  if truck_w:
    if sum(bridge_queue) + truck_w[0] <= l:
      t = truck_w.popleft()
      bridge_queue.append(t)
    else:
      bridge_queue.append(0)
    

  if not bridge_queue:
    break

print(time)