def solution(cost, hint):
    answer = float('inf')  
    # 각 스테이지 별 보유중인 힌트권 개수
    have_hints = [0] * len(cost)
    
    def dfs(stage, money):
        nonlocal answer
        
        # 현재 비용이 이미 찾은 최소비용보다 클 경우 탐색을 종료한다(가지치기) 
        if money > answer:
            return 
        # 모든 스테이지를 다 탐색했을 경우 최솟값을 갱신한다
        if stage == len(cost):
            answer = min(answer, money)
            return
        
        # 보유한 힌트권 개수가 해당 스테이지에서 사용 가능한 최대 개수 이상이면 최대로 사용할 수 있는 개수만큼만 사용
        used_hints = have_hints[stage]
        if used_hints >= len(cost[stage]):
            used_hints = len(cost[stage]) - 1
            
        stage_clear_cost = cost[stage][used_hints]
        next_money = money + stage_clear_cost
        
        # 클리어 후 비용이 이미 최솟값 이상이면 탐색을 멈춘다
        if next_money >= answer:
            return
        # 마지막 스테이지는 구매할 수 있는 힌트 번들이 없으므로 바로 다음 단계로 진행한다
        if stage == len(cost) - 1:
            dfs(stage + 1, next_money)
            return
            
        # 힌트 번들을 구매하지 않는 경우
        dfs(stage + 1, next_money)   
        
        # 힌트 번들을 구매하는 경우
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