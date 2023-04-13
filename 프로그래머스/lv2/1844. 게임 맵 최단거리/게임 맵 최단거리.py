from collections import deque

def solution(maps):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    col_length = len(maps[0])
    row_length = len(maps)
    visited = [[0 for col in range(col_length)] for row in range(row_length)]
    
    queue = deque([])
    queue.append((0,0))
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= row_length or ny >= col_length:
                continue
                
            if maps[nx][ny] == 0:
                continue
                
            if visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] += visited[x][y] + 1

    if visited[-1][-1] == 0:
        return -1
    else:
        return visited[-1][-1]