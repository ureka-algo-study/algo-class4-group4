def solution(cap, n, deliveries, pickups):
    answer = 0   
    # 앞선 방문(더 먼 집)에서 남겨온 배달/수거 가능 여유 용량
    current_deliver = 0
    current_pickup = 0
    
    # 가장 먼 집(n-1)부터 0번째 집까지 거꾸로 탐색 (그리디 알고리즘)
    for i in range(n-1, -1, -1):
        # 현재 집의 배달/수거해야 할 물량을 여유 용량에서 뺀다.
        current_deliver -= deliveries[i]
        current_pickup -= pickups[i]
        
        visit_count = 0
        # 배달/수거 중 어느 하나라도 값이 음수가 되었다면 이 집을 방문하기 위해 트럭이 재출발해야 한다는 의미다.
        while current_deliver < 0 or current_pickup < 0:
            current_deliver += cap
            current_pickup += cap
            visit_count += 1
        
        # 현재 누적 이동거리에 "(index + 1) * 2(왕복) * visit_count(방문 횟수)" 값을 누적해서 더해준다.
        answer += (i+1) * visit_count * 2
    
    return answer