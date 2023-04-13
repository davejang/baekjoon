def solution(genres, plays):
    answer = []
    genre_played = {}
    genre_rank = []
    index = []
    
    for i in range(len(genres)):
        index.append(i)
    play_info = list(zip(genres,plays,index))
    play_info = sorted(play_info, key=lambda x:(x[0],-x[1],x[2]))
    
    # 장르 별 재생 순위 집계
    for i in range(len(genres)):
        # index_genre[i] = genres[i]
        if not genres[i] in genre_played:
            genre_played[genres[i]] = plays[i]
        else:
            genre_played[genres[i]] += plays[i]
    
    # 장르 별 순위 리스트 추출(총 플레이 수 내림차순)
    for i in sorted(genre_played.items(), key=lambda x:-x[1]):
        genre_rank.append(i[0])
        
    print(play_info)
    print(genre_rank)
    
    for g in genre_rank:
        count = 0
        for info in play_info:
            if info[0] == g:
                count += 1
                answer.append(info[2])
                if count == 2:
                    break
                

    
    return answer