t = int(input())
for i in range(t):
  n = int(input())
  max_price = 0
  result = 0
  stock_price = list(map(int,input().split()))
  for j in range(n-1,-1,-1):
    if stock_price[j] > max_price:
      max_price = stock_price[j]
    else:
      result += max_price - stock_price[j]
  print(result)