import sys
import heapq

input = sys.stdin.readline

t = int(input())

for i in range(t):
  left_q = []
  right_q = []
  m = int(input())
  arr = []
  for i in range(m//10 + 1):
    arr += list(map(int,input().rstrip().split()))
  midean_list =[]

  for i in range(0,len(arr)):
    if not right_q:
      heapq.heappush(right_q,arr[i])
    elif arr[i] < right_q[0]:
      heapq.heappush(left_q,-1*arr[i])
    else:
      heapq.heappush(right_q,arr[i])
    
    if len(left_q) > len(right_q):
      heapq.heappush(right_q,-heapq.heappop(left_q))
    elif len(left_q) + 1 < len(right_q):
      heapq.heappush(left_q,-heapq.heappop(right_q))

    if i % 2 == 0:
      midean_list.append(right_q[0])
      
  print(m//2+1)
  for i in range((m//2+1)//10 + 1):
    for j in range(10):
      print(midean_list[j+10*i],end = ' ')
      if j+10*i >= m//2:
        break
    print()