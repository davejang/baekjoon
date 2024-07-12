import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
q = []
result = 0

for i in range(n):
    day, price = map(int,input().split())
    arr.append((day,price))
arr.sort(key=lambda x:(x[0],-x[1]))
    
for day, price in arr:
    if not q:
        heapq.heappush(q,(price,day))
    else:
        if len(q) < day:
            heapq.heappush(q,(price,day))
        else:
            if q[0][0] < price:
                heapq.heappop(q)
                heapq.heappush(q,(price,day))
                
for price, day in q:
    result += price
print(result)