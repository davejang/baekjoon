import sys

input = sys.stdin.readline

arr = []
result = 0

n = int(input())
for i in range(n):
  position, height = map(int,input().split())
  arr.append((position,height))
  
arr.sort(key= lambda x:x[1])
max_position = arr[-1][0]
max_height = arr[-1][1]

result += max_height

arr.sort(key= lambda x:x[0])
temp_p_right = arr[0][0]
temp_h_right = arr[0][1]

for p, h in arr:
  if h >= temp_h_right:
    result += abs(temp_p_right - p) * temp_h_right
    temp_p_right = p
    temp_h_right = h

  if temp_h_right == max_height and temp_p_right == max_position:
    break

arr.sort(key= lambda x:x[0],reverse=True)
temp_p_left = arr[0][0]
temp_h_left = arr[0][1]
for p, h in arr:
  if h >= temp_h_left:
    result += abs(temp_p_left - p) * temp_h_left
    temp_p_left = p
    temp_h_left = h

  if temp_h_left == max_height and temp_p_left == max_position:
    break

print(result)