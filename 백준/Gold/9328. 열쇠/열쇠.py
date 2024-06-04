import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    count = 0
    q = deque()
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h+2 and 0 <= ny < w+2 and visited[nx][ny] == False:
                if graph[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif ord('a') <= ord(graph[nx][ny]) <= ord('z'):
                    key_list.append(graph[nx][ny])
                    q = deque()
                    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
                    graph[nx][ny] = '.'
                    q.append((nx,ny))
                elif ord('A') <= ord(graph[nx][ny]) <= ord('Z'):
                    if chr(ord(graph[nx][ny]) + 32) in key_list:
                        visited[nx][ny] = True
                        graph[nx][ny] = '.'
                        q.append((nx,ny))
                elif graph[nx][ny] == '$':
                    visited[nx][ny] = True
                    count += 1
                    graph[nx][ny] = '.'
                    q.append((nx,ny))
    
    print(count)

t = int(input())

for i in range(t):
    h, w = map(int,input().split())
    graph = []
    key_list = []
    
    for j in range(h):
        graph.append(list(str(input().rstrip())))
    key = str(input().rstrip())
    if key != '0':
        key_list = list(key)
        
    for row in graph:
        row.insert(0, '.')
        row.append('.')
    graph.insert(0, ['.']*(w+2))
    graph.append(['.']*(w+2))
    
    bfs(0,0)
    