n, m = map(int,input().split())

price = []

for i in range(m):
  a = int(input())
  price.append(a)

price.sort()

result = 0
current_price = 0

for i in range(len(price)):
  if(price[i] * (m-i) > result and m-i <= n):
    result = price[i] * (m-i)
    current_price = price[i]

print(current_price,result)