import itertools

n, k = map(int,input().split())
word_list = []
basic_set = set(['a','n','t','i','c'])
chr_set = []
result = 0

for i in range(n):
  word = str(input())
  middle_chr = list(word[4:-4])
  chr_set += middle_chr
  word_list.append(word)

chr_set = list(set(chr_set) - basic_set)

if k < 5:
  print(0)
else:
  word_study = list(itertools.combinations(chr_set,k-5))
  if word_study == []:
    print(n)
  else:
    for study_case in word_study:
      can_read = 0
      study_case = list(study_case)
      learn_word = list(basic_set) + study_case
      for word in word_list:
        readable = True
        for i in range(4,len(word)-4):
          if word[i] not in learn_word:
            readable = False
            break
        if readable == True:
          can_read += 1
      result = max(result,can_read)
    print(result)