import sys

input = sys.stdin.readline

arr = []
result = 0
n, l = map(int,input().split())
for i in range(n):
  arr.append(list(map(int,input().rstrip().split())))

def check_route(route):
  curr_h = route[0]
  slope = [0] * n
  
  for i in range(1,n):
    # 경사가 같거나 경사로 설치된 경우
    if curr_h - route[i] == 0 or slope[i] == 1:
      continue

    # 경사가 1보다 클 경우 False
    if abs(curr_h - route[i]) > 1:
      return 0

    # 경사 차이 1
    if abs(curr_h - route[i]) == 1:
      # 경사로 길이
      length = l
      
      # 경사가 낮을 경우 오른쪽 탐색
      if curr_h > route[i]:
        right = route[i+1:]
        length -= 1

        for j in range(len(right)):
          if length == 0:
            break
          if slope[i+j] == 1 or route[i] != right[j]:
            return 0
          if route[i] == right[j]:
            length -= 1
            
        if length == 0:
          for k in range(l):
            slope[i+k] = 1
        else:
          return 0

      # 경사가 높을 경우 왼쪽 탐색
      if curr_h < route[i]:
        left = route[:i]
        left.reverse()
        
        for j in range(len(left)):
          if slope[i-j-1] == 1 or route[i] != left[j] + 1:
            return 0
          if route[i] == left[j] + 1:
            length -= 1
          if length == 0:
            break
            
        if length == 0:
          for k in range(l):
            slope[i-k-1] = 1
        else:
          return 0

      # 현재 경사 갱신
      curr_h = route[i]

  return 1

for i in range(n):
  col = arr[i]
  result += check_route(col)

for i in range(n):
  row = []
  for j in range(n):
    row.append(arr[j][i])
  result += check_route(row)

print(result)