import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b,group):
    result = []
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    cnt = 1
    
    while q:
        x, y = q.popleft()
        result.append((x,y))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == '0':
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx,ny))
                   
    for i, j in result:
        count[i][j][0] = cnt
        count[i][j][1] = group
                    
n, m = map(int,input  ().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
answer = [[0 for _ in range(m)] for _ in range(n)]
count = [[[0,0] for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph.append(list(input().rstrip()))

group = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and visited[i][j] == False:
            group += 1
            bfs(i,j,group)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            group_list = []
            for c in range(4):
                x = i + dx[c]
                y = j + dy[c]
                if 0 <= x < n and 0 <= y < m:
                    if count[x][y][1] not in group_list:
                        answer[i][j] += count[x][y][0]
                        group_list.append(count[x][y][1])
            answer[i][j] += 1
            answer[i][j] = answer[i][j] % 10
            
for i in answer:
    ans = list(map(str,i))
    print(''.join(ans))