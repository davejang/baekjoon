n = int(input())
arr = list(map(int,input().split()))
opr = list(map(int,input().split()))
result_list = []
min_val = 1e9
max_val = -1e9

def calculate(i,cal):
  global min_val, max_val, n
  if i == n - 1:
    min_val = min(min_val,cal)
    max_val = max(max_val,cal)
  else:
    if opr[0] > 0:
      opr[0] -= 1
      calculate(i+1,cal + arr[i+1])
      opr[0] += 1
    if opr[1] > 0:
      opr[1] -= 1
      calculate(i+1,cal - arr[i+1])
      opr[1] += 1
    if opr[2] > 0:
      opr[2] -= 1
      calculate(i+1,cal * arr[i+1])
      opr[2] += 1
    if opr[3] > 0:
      opr[3] -= 1
      calculate(i+1,int(cal / arr[i+1]))
      opr[3] += 1
      
calculate(0,arr[0])

print(max_val)
print(min_val)