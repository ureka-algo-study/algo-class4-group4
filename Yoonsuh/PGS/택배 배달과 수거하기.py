def solution(cap, n, deliveries, pickups):
    dist = 0
    delivery = 0  # 미처리 배달 누적
    pickup = 0    # 미처리 수거 누적

    for i in range(n - 1, -1, -1):  # 가장 먼 집부터 역순
        delivery += deliveries[i]    # i번 집 배달량 누적
        pickup += pickups[i]         # i번 집 수거량 누적

        while delivery > 0 or pickup > 0:  # 잔량 남으면 왕복 추가
            delivery -= cap   # 이번 왕복에 cap만큼 배달
            pickup -= cap     # 이번 왕복에 cap만큼 수거
            dist += (i + 1)   # i+1 = 1-indexed 거리(왕복은 마지막에 ×2)

    return dist * 2  # 왕복이므로 ×2