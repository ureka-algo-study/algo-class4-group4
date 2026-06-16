def solution(stones, k):
    
    # mid(명)이 징검다리를 건널 수 있는지를 확인하는 함수
    def cross(mid):
        cnt = 0
        
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                # k명이 연속으로 건너지 못하면 return False
                if cnt >= k:
                    return False
            else:
                cnt = 0
        return True
    
    # 이진 탐색 알고리즘을 사용해 징검다리를 건널 수 있는 최대 인원을 탐색한다.
    low, high = 1, max(stones)
    answer = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if cross(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return answer