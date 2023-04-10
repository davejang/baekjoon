def solution(nums):
    # 포켓몬 종류 (set을 활용해 중복 제거)
    type_number = len(set(nums)) 
    # 가져갈 수 있는 최대 포켓몬 개수
    poke_number = len(nums)//2
    
    answer = min(type_number,poke_number)
    
    return answer