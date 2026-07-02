# 오답 풀이
# 정확성 테스트 : 42.9 / 효율성 테스트 : 0.0

def solution(food_times, k):

    idx = 0
    second = 0
    
    while second <= k:
        idx %= len(food_times)
        if sum(food_times) == 0:
            return -1
        if food_times[idx] > 0:
            food_times[idx] -= 1
            idx += 1
            second += 1
        else:
            idx += 1
            
    return idx