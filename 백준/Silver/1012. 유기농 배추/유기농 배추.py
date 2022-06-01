import sys
sys.setrecursionlimit(10000)
T = int(input())
result_list = []

def dfs(a,b):
  if a <= -1 or a >= m or b <= -1 or b >= n:
    return False
  if graph[a][b] == 1:
    graph[a][b] = 0
    dfs(a-1,b)
    dfs(a,b-1)
    dfs(a+1,b)
    dfs(a,b+1)
    return True
  return False
  
for i in range(T):
  n, m, k = map(int,input().split())
  result = 0
  graph = [[0 for i in range(n)] for i in range(m)]
  for j in range(k):
    a, b = map(int,input().split())
    graph[b][a] = 1
    
  for i in range(n):
    for j in range(m):
      if dfs(j,i) == True:
        result += 1
  result_list.append(result)
for i in result_list:
  print(i)
