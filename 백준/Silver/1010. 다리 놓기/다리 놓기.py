n = int(input())
Testcase = []
factorials = [0]* 31
factorials[0] = 1
factorials[1] = 1

for i in range(1,31):
  factorials[i] = i * factorials[i-1]

for i in range(n):
  n, m = map(int,input().split())
  result = factorials[m] / (factorials[m-n] * factorials[n])
  Testcase.append(int(result))

for i in Testcase:
  print(i)