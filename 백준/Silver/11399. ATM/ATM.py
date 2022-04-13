n = int(input())
time = list(map(int,input().split()))
time_take = []
result = 0
a = 0

time.sort()

for i in range(n):
  if(i > 0):
    for j in range(i+1):
      a = a + time[j]
    time_take.append(a)
    a = 0
  else:
    time_take.append(time[i])
  result = result + time_take[i]

print(result)