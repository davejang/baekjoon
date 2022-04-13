exp = input()
num = []
result = 0

a = exp.split("-")

for i in range(len(a)):
  b = a[i].split("+")
  for j in range(len(b)):
    if(i==0):
      result = result + int(b[j])
    else:
      result = result - int(b[j])

print(result)