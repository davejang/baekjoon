T = int(input())
TestCase = []

for i in range(T):
  TestCase.append(int(input()))
memory_zero = [1,0,1]
memory_one = [0,1,1]

def fibo(x):
  start = len(memory_zero)
  if x >= start:
    for i in range(start,x+1):
      memory_zero.append(int(memory_zero[i-1]+memory_zero[i-2]))
      memory_one.append(int(memory_one[i-1]+memory_one[i-2]))
      
for i in TestCase:
  if len(memory_zero) <= i:
    fibo(i)
  print(memory_zero[i],memory_one[i])
