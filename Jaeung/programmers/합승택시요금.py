def solution(n, s, a, b, fares):
    INF = float('inf')
    answer = INF
    # i에서 j까지 가는 최저 택시 요금을 저장한다.
    taxi = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        taxi[i][i] = 0
    
    for fare in fares:
        taxi[fare[0]][fare[1]] = fare[2]
        taxi[fare[1]][fare[0]] = fare[2]

    for k in range(n+1): # 중간 지점
        for i in range(n+1): # 출발 지점
            for j in range(n+1): # 도착 지점
                # 기존에 발견한 최단 거리(i -> j)와 k를 거쳐가는 새로운 경로 중에서 최솟값을 구해 최저 택시 요금을 갱신한다.
                taxi[i][j] = min(taxi[i][k] + taxi[k][j], taxi[i][j])
    
    # 두 사람이 출발 지점(s)에서 중간 지점(t)까지 합승하고, 이후 각자의 도착 지점(a, b)으로 따로 이동하는 모든 경우를 고려한다.
    # 이 경우에서 택시 요금이 최저로 나오는 경우를 answer에 기록한다.
    for t in range(1, n+1):
        tmp = taxi[s][t] + taxi[t][a] + taxi[t][b]
        answer = min(tmp, answer)
        
    return answer
    