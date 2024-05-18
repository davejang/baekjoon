import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
result = [arr[0]]

def binary_search(x):
    start = 0
    end = len(result) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if result[mid] == x:
            return mid
        elif result[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
            
    return start
            
for item in arr:
    if result[-1] < item:
        result.append(item)
    else:
        idx = binary_search(item)
        result[idx] = item
        
print(len(result))