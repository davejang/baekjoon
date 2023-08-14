import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
home = []
chicken = []
answer = int(1e9)

def cal(x1,y1,x2,y2):
  return abs(x2-x1) + abs(y2-y1)

for i in range(n):
  graph.append(list(map(int,input().rstrip().split())))

for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      chicken.append((i,j))
    if graph[i][j] == 1:
      home.append((i,j))

for comb in combinations(chicken,m):
  total_dist = 0
  for x1, y1 in home:
    dist = int(1e9)
    for x2, y2 in comb:
      dist = min(dist,cal(x1,y1,x2,y2))
    total_dist += dist
  answer = min(answer,total_dist)

print(answer)