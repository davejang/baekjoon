n, k = map(int,input().split())

money = k
coin_list = []
count = 0

for i in range(n):
  coin = int(input())
  coin_list.append(coin)
  if(coin <= k):
    max_index = i

while(1):
  temp = int(money / coin_list[i])
  if(temp > 0):
    count = count + temp
    money = money - temp * coin_list[i]
  if(money == 0):
    break
  i = i -1

print(count)