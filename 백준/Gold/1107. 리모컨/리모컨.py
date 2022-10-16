import itertools

current_chanel = 100

n = int(input())
m = int(input())
if m > 0:
  broken = list(map(str,input().split()))
  number = list(set(['1','2','3','4','5','6','7','8','9','0']) - set(broken))
  
  case_list = []
  for i in range(1,len(str(n))+2):
    case_list += list(itertools.product(number,repeat=i))
  
  result = 100000001
  
  for case in case_list:
    if case[0] == '0' and len(case) > 1:
      continue
    chanel = ''.join(case)
    
    button_count = abs(n-int(chanel)) + len(chanel)
  
    result = min(button_count,result)
  
  result = min(result,abs(100-n))
  print(result)
else:
  print(min(len(str(n)),abs(100-n)))