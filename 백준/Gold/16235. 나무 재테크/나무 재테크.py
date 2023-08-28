import sys
from collections import deque

input = sys.stdin.readline
dx = [1,1,1,0,-1,-1,-1,0]
dy = [1,0,-1,-1,-1,0,1,1]

n, m, k = map(int,input().split())

tree_queue = []
feed = [[5 for _ in range(n)] for _ in range(n)]
arr = [[deque() for _ in range(n)] for _ in range(n)]
s2d2 = []
for i in range(n):
  s2d2.append(list(map(int,input().rstrip().split())))

for i in range(m):
  x, y, z = map(int,input().split())
  arr[x-1][y-1].append(z)

while k > 0:
  feed_queue = []

  # 봄 + 여름
  for r in range(n):
    for c in range(n):
      tree_list = arr[r][c]
      new_tree_list = deque()
      feed_amount = 0
      for tree in tree_list:
        if tree <= feed[r][c]:
          feed[r][c] -= tree
          tree += 1
          new_tree_list.append(tree)
        else:
          feed_queue.append((r,c,tree//2))
          feed_amount += tree//2
      feed[r][c] += feed_amount
      arr[r][c] = new_tree_list

  # 가을 + 겨울
  for r in range(n):
    for c in range(n):
      tree_list = arr[r][c]
      for tree in tree_list:
        if tree % 5 == 0:
          for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= n:
              continue
            arr[nx][ny].appendleft(1)

      feed[r][c] += s2d2[r][c]
  
  k -= 1

result = 0
for r in range(n):
  for c in range(n):
    result += len(arr[r][c])

print(result)