import sys
from collections import defaultdict

input = sys.stdin.readline

graph = []
answer = -1
count = 0

r, c, k = map(int,input().split())
for i in range(3):
  graph.append(list(map(int,input().split())))

def calculate():
  global graph
  length = 0
  
  new_graph = []
  for graph_col in graph:
    num_dict = defaultdict(int)
    temp = []
    new_col = []

    # Count
    for i in graph_col:
      if i == 0:
        continue
      num_dict[i] += 1

    for i in num_dict:
      temp.append((i,num_dict[i]))
      
    # 정렬
    temp.sort(key = lambda x:(x[1],x[0]))
    # 원소 100개 초과할 경우 버림
    if len(temp) > 50:
      temp = temp[:50]
    
    for i in temp:
      new_col.append(i[0])
      new_col.append(i[1])

    length = max(length,len(new_col))

    new_graph.append(new_col)

  graph = new_graph

  for graph_col in graph:
    if len(graph_col) < length:
      for i in range(len(graph_col),length):
        graph_col.append(0)

while count <= 100:
  if r - 1 < len(graph) and c - 1 < len(graph[0]):
    if graph[r-1][c-1] == k:
      answer = count
      break

  count += 1
  # R연산
  if len(graph) >= len(graph[0]):
    calculate()
  # C연산 : Transpose -> R연산 -> Transpose
  else:
    graph = list(map(list, zip(*graph)))
    calculate()
    graph = list(map(list, zip(*graph)))

print(answer)