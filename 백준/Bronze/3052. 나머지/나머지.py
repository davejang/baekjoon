array = []
for i in range(10):
  number = int(input())
  array.append(number%42)
diff = set(array)
print(len(diff))