def solution(stones, k):
    left = 0
    right = 200000000
    
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        
        count = 0
        for i in temp:
            if i - mid <= 0:
                count += 1
            else:
                count = 0
            if count >= k:
                break
        
        if count >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left