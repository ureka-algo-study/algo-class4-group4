import heapq

def solution(n, paths, gates, summits):
    hq = []
    INF = float('inf')
    dist = [INF] * (n+1)  # dist[x] : x 지점까지 도달하는 등산코스의 intensity 값
    answer = [0, INF]
    summits.sort()  # intensity가 최소가 되는 등산코스가 여러 개인 경우, 작은 번호가 먼저 선택되도록 정렬한다.
    
    # 등산로는 양방향이므로 양쪽에 모두 추가
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    
    # 모든 게이트를 intensity 0으로 큐에 동시에 넣어 한 번에 탐색한다.
    for gate in gates:
        heapq.heappush(hq, (0, gate))
        dist[gate] = 0
        
    while hq:
        intensity, node = heapq.heappop(hq)
        # 산봉우리에 도달했거나 이미 더 작은 값으로 갱신이 된 경우, 가지치기한다.
        if intensity > dist[node] or node in summits:
            continue
        for next_intensity, next_node in graph[node]:
            # 이번 경로의 이동시간이 누적 intensity 값보다 더 크거나 같은 경우에는 next_intensity로 값을 갱신한다.
            if intensity <= next_intensity and dist[next_node] > next_intensity:
                dist[next_node] = next_intensity
                heapq.heappush(hq, (next_intensity, next_node))
            # 지금까지의 누적값이 더 큰 경우에는 intensity 값을 그대로 유지한다.
            elif intensity > next_intensity and dist[next_node] > intensity:
                dist[next_node] = intensity
                heapq.heappush(hq, (intensity, next_node))
    
    # intensity 값이 최소가 되는 등산코스의 산봉우리 번호와 intensity 값을 정답으로 선택한다.
    for summit in summits:
        if dist[summit] < answer[1]:
            answer[0] = summit
            answer[1] = dist[summit]

    return answer