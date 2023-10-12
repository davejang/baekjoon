import sys

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
alphabet = set()
result = 0

r, c = map(int,input().split())
for i in range(r):
  graph.append(list(str(input().rstrip())))

def dfs(x,y,count):
  global result
  result = max(result,count)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in alphabet:
      alphabet.add(graph[nx][ny])
      dfs(nx,ny,count+1)
      alphabet.remove(graph[nx][ny])

alphabet.add(graph[0][0])
dfs(0,0,1)
print(result)