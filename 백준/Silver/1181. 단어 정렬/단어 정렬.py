n = int(input())
array = []

for i in range(n):
  data = str(input())
  if (data in array) == False:
    array.append(data)
    
array.sort()
array.sort(key=len)
for i in array:
  print(i)