import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
position = list(map(int,input().split()))
position.sort()
arr = []
for i in range(n-1):
    arr.append(position[i+1] - position[i])
    
arr.sort()
print(sum(arr[:n-k]))