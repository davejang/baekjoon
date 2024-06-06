import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(x,y,dx,dy):
    cnt = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    
    return x, y, cnt
        
def bfs(ball):
    red_x, red_y = ball[0]
    blue_x, blue_y = ball[1]
    
    visited = []
    visited.append((red_x,red_y,blue_x,blue_y))
    q = deque()
    q.append((red_x,red_y,blue_x,blue_y,1))
    
    while q:
        rx, ry, bx, by, count = q.popleft()
        
        if count > 10:
            break

        for i in range(4):
            rnx, rny, rcnt = move(rx,ry,dx[i],dy[i])
            bnx, bny, bcnt = move(bx,by,dx[i],dy[i])
            
            if graph[bnx][bny] == "O":
                continue
            if graph[rnx][rny] == "O":
                print(count)
                return
            
            if rnx == bnx and rny == bny:
                if rcnt > bcnt:
                    rnx -= dx[i]
                    rny -= dy[i]
                else:
                    bnx -= dx[i]
                    bny -= dy[i]

            if (rnx,rny,bnx,bny) not in visited:
                visited.append((rnx,rny,bnx,bny))
                q.append((rnx,rny,bnx,bny,count+1))
            
    print(-1)

n, m = map(int,input().split())
ball = [[0,0],[0,0]]
graph = []
for i in range(n):
    graph.append(list(input().rstrip()))
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            ball[0] = [i,j]
        if graph[i][j] == 'B':
            ball[1] = [i,j]
            
bfs(ball)