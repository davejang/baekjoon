n = int(input())

max_weight = []
temp = 0
result = 0

for i in range(n):
  m = int(input())
  max_weight.append(m)

max_weight.sort(reverse=True)

for k in range(n):
  temp = max_weight[k] * (k + 1)
  if(result < temp):
    result = temp

print(result)