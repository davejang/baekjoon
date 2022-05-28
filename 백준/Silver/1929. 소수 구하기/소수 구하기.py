a, b = map(int,input().split())
array = [0]*(b+1)
array[1] = 1

for i in range(2,len(array)):
  if array[i] == 0:
    for j in range(i+i,len(array),i):
      array[j] = 1

for i in range(a,b+1):
  if array[int(i)] == 0:
    print(i)