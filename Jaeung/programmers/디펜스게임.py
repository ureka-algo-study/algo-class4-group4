import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    answer = []
    for i in range(len(enemy)):
        heapq.heappush(answer, enemy[i])
        if len(answer) > k:
            last = heapq.heappop(answer)
            if last > n:
                return i
            n -= last
    
    return len(enemy)