x, y = map(int,input().split())

days = [31,28,31,30,31,30,31,31,30,31,30,31]
n = 0

for i in range(x-1):
  n = n + days[i]
n = n + y
if n % 7 == 1:
  print("MON")
if n % 7 == 2:
  print("TUE")
if n % 7 == 3:
  print("WED")
if n % 7 == 4:
  print("THU")
if n % 7 == 5:
  print("FRI")
if n % 7 == 6:
  print("SAT")
if n % 7 == 0:
  print("SUN")
