import sys
import copy
from collections import deque

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
result = 0

n, m, d = map(int,input().split())
for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

# 적 유무 확인
def check_empty():
  for i in range(n):
    for j in range(m):
      if temp_graph[i][j] == 1:
        return False

  return True

# 적 이동
def move():
  for i in range(-1,-n,-1):
    temp_graph[i] = temp_graph[i-1]
  temp_graph[0] = [0 for _ in range(m)]

# 게임 진행
def game(a,b,c):
  global result
  count = 0
  archer_list = [(n,a),(n,b),(n,c)]

  while True:
    if check_empty():
      break
    count += attack(archer_list)
    move()

  result = max(result,count)

# 궁수의 공격 (동시에 공격)
def attack(archer_list):
  global d
  count = 0
  attack_cand = []

  for archer in archer_list:
    enemy_list = []
    for i in range(n):
      for j in range(m):
        if temp_graph[i][j] == 1:
          distance = abs(i - archer[0]) + abs(j - archer[1])
          if distance <= d:
            enemy_list.append((distance,i,j))
    enemy_list.sort(key=lambda x:(x[0],x[2]))
    if enemy_list:
      attack_cand.append(enemy_list[0])

  for enemy in attack_cand:
    if temp_graph[enemy[1]][enemy[2]] == 1:
      temp_graph[enemy[1]][enemy[2]] = 0
      count += 1

  return count
    
for a in range(m-2):
  for b in range(a+1,m-1):
    for c in range(b+1,m):
      temp_graph = copy.deepcopy(graph)
      game(a,b,c)

print(result)