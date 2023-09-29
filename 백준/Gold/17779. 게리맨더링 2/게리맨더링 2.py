import sys

input = sys.stdin.readline
INF = int(1e9)

graph = []
n = int(input())
total = 0
result = INF
for i in range(n):
  col = list(map(int,input().rstrip().split()))
  graph.append(col)
  total += sum(col)

# 경계선 길이 설정
def set_border(x,y):
  for d1 in range(1,n):
    for d2 in range(1,n):
      if x + d1 + d2 > n-1:
        continue
      if y - d1 < 0:
        continue
      if y + d2 > n-1:
        continue
      area(x,y,d1,d2)

# 구역 설정
def area(x,y,d1,d2):
  global result
  
  people = [0] * 5
  area_graph = [[0 for _ in range(n)] for _ in range(n)]
  area_graph[x][y] = 5
  for i in range(d1+1):
    area_graph[x+i][y-i] = 5
  for i in range(d2+1):
    area_graph[x+i][y+i] = 5
  for i in range(d2+1):
    area_graph[x+d1+i][y-d1+i] = 5
  for i in range(d1+1):
    area_graph[x+d2+i][y+d2-i] = 5

  # 2, 4번 선거구는 역순으로 탐색해야 함
  # 1번 선거구
  for r in range(x+d1):
    for c in range(y+1):
      if area_graph[r][c] == 5:
        break
      people[0] += graph[r][c]

  # 2번 선거구
  for r in range(x+d2+1):
    for c in range(n-1,y,-1):
      if area_graph[r][c] == 5:
        break
      people[1] += graph[r][c]

  # 3번 선거구
  for r in range(x+d1,n):
    for c in range(y-d1+d2):
      if area_graph[r][c] == 5:
        break
      people[2] += graph[r][c]

  # 4번 선거구
  for r in range(x+d2+1,n):
    for c in range(n-1,y - d1 + d2 -1,-1):
      if area_graph[r][c] == 5:
        break
      people[3] += graph[r][c]
      
  people[4] = total - sum(people)
  
  result = min(result,max(people) - min(people))

for i in range(n):
  for j in range(n):
    set_border(i,j)

print(result)