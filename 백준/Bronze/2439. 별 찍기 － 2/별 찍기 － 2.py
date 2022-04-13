n = int(input())

for i in range(1,n+1):
  if(i<n):
    print(" " * (n - 1 - i), "*" * i)
  else:
    print("*" * i)