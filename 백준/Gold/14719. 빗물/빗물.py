h, w = map(int,input().split())
block = list(map(int,input().split()))
result = 0
 
for i in range(1,w-1):
  left_pillar = max(block[:i])
  right_pillar = max(block[i+1:])
  water_level = min(left_pillar,right_pillar)

  if water_level > block[i]:
    result += water_level - block[i]

print(result)