from collections import deque

INF = int(1e9)

def solution(board):
    
    def bfs(start):
        length = len(board)
        cost_memo = [[INF for _ in range(len(board))] for _ in range(len(board))]
        cost = 0
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        q = deque([start])

        while q:
            x, y, cost, d = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
                    if i == d:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600
                    if ncost < cost_memo[nx][ny]:
                        cost_memo[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])

        return cost_memo[-1][-1]
                
    return min(bfs((0, 0, 0, 1)), bfs((0, 0, 0, 3)))