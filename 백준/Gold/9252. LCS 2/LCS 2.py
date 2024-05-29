import sys

input = sys.stdin.readline

s1 = [0] + list(input().rstrip())
s2 = [0] + list(input().rstrip())
arr = [['' for _ in range(len(s1))] for _ in range(len(s2))]

for i in range(1,len(s2)):
    for j in range(1,len(s1)):
        if s1[j] == s2[i]: 
            arr[i][j] = arr[i-1][j-1] + s1[j]
        else:
            if len(arr[i][j-1]) > len(arr[i-1][j]):
                arr[i][j] = arr[i][j-1]
            else:
                arr[i][j] = arr[i-1][j]
                
answer = len(arr[-1][-1])
print(answer)
if answer > 0:
    print(arr[-1][-1])