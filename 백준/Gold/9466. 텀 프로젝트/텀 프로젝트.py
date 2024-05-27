import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x):
    global result
    
    visited[x] = True
    cycle.append(x)
    
    if visited[graph[x]]:
        if graph[x] in cycle:
            result -= len(cycle[cycle.index(graph[x]):])
    else:
        dfs(graph[x])


t = int(input())
for i in range(t):
    n = int(input())
    result = n
    visited = [False] * (n+1)
    graph = [0] + list(map(int,input().split()))
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
        
    print(result)