n = int(input())
array = [0]*1001
array[1] = 1
result = 0
number = input().split()

for i in range(2,len(array)):
  if array[i] == 0:
    for j in range(i+i,len(array),i):
      array[j] = 1

for i in number:
  if array[int(i)] == 0:
    result= result + 1
print(result)