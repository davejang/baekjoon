import sys
n = int(input())
array = [0]*10001

for i in range(n):
  number = int(sys.stdin.readline())
  array[number] = array[number] + 1

for i in range(len(array)):
  if i != 0:
    for j in range(array[i]):
      print(i)