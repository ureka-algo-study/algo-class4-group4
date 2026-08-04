def solution(cost, hint):
    answer = float('inf')  
    n = len(cost)
    # 각 스테이지 별 보유중인 힌트권 개수
    have_hints = [0] * n
    
    def dfs(stage, money):
        nonlocal answer
        # 모든 스테이지를 다 탐색했을 경우 최솟값을 갱신한다
        if stage == n:
            answer = min(answer, money)
            return
        
        used_hints = min(have_hints[stage], len(cost[stage]) - 1)
        next_money = money + cost[stage][used_hints]
        # 클리어 후 비용이 이미 최솟값 이상이면 탐색을 멈춘다
        if next_money >= answer:
            return
        
        # 힌트 번들을 구매하지 않는 경우
        dfs(stage + 1, next_money)  
        
        # 힌트 번들을 구매하는 경우(구매 가능한 번들이 있는 경우에만 시도)
        if stage < n - 1:
            bundle = hint[stage]
            bundle_price = bundle[0]
            bundle_hints = bundle[1:]   
            # 번들 구매 비용을 더해 다음 단계로 진행 
            # -> 이후 다른 경로 탐색을 위해 획득했던 힌트권을 다시 차감(복구)
            for h in bundle_hints:
                have_hints[h - 1] += 1        
            dfs(stage + 1, next_money + bundle_price)
            for h in bundle_hints:
                have_hints[h - 1] -= 1
            
    dfs(0, 0)    
    return answer