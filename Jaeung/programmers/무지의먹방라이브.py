# 정답 풀이

# 남은 음식 중 섭취 시간(food_time)이 가장 작은 음식을 기준으로, "이 음식을 다 먹을 때까지 몇 바퀴가 돌아야 하는가"를 구하는 아이디어

import heapq
def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1    
    
    q = []
    length = len(food_times)  # 남은 음식 개수
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))        
    
    previous = 0   # 이전에 다 먹은 음식의 food_time        
    # q[0][0] : 남은 음식 중 food_time이 가장 작은 음식
    while (q[0][0] - previous) * length <= k:
        # 먹는데 가장 적게 걸리는 음식을 다 먹을 때까지 소요된 시간을 빼준다.
        k -= (q[0][0] - previous) * length
        length -= 1
        previous, _ = heapq.heappop(q)
        
    result = sorted(q, key = lambda x : x[1])
    # 남은 음식 length개를 같은 순서로 반복해서 먹다가 멈추는 음식에서 번호를 찾는다.
    answer = result[k % length][1]
    
    return answer     


# ------------------------------


# 오답 풀이
# 정확성 테스트 : 42.9 / 효율성 테스트 : 0.0

"""
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
"""
