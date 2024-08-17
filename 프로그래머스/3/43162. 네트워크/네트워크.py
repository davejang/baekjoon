def solution(n, computers):
    parents = [i for i in range(n)]
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
                
    for i in range(n):
        for node in graph[i]:
            union(parents, i, node)
            
    for i in range(n):
        find_parent(parents,i)
    
    return len(set(parents))

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    
    if(a < b):
        parents[b] = a
    else:
        parents[a] = b
