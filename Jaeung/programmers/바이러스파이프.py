from collections import deque

def solution(n, infection, edges, k):
    
    def infect(curr_set, pipe_type):
        new = set(curr_set)
        queue = deque(list(curr_set))
        
        while queue:
            node = queue.popleft()
            for neighbor, t in graph[node]:
                # 아직 노드가 감염이 안 되었고 / 선택한 파이프 타입(pipe_type)과 일치하는 경우
                if neighbor not in new and t == pipe_type:
                    new.add(neighbor)
                    queue.append(neighbor)
        return new                
           
    graph = [ [] for _ in range(n+1)] 
    for x, y, t in edges:
        graph[x].append((y, t))
        graph[y].append((x, t))

    maximum = 0
    init = set([infection])
    # (현재 감염된 node들의 set, 행동 횟수)
    q = deque([(init, 0)])
    
    # 중복 상태 확인을 위해 tuple 형태로 변환해서 저장
    visited = set()
    visited.add(tuple(sorted(list(init))))
    
    while q:
        curr, count = q.popleft()
        maximum = max(len(curr), maximum)
        
        # k번(최대) 파이프를 열었다 닫았거나 / 배양체가 전부 다 감염되었으면 탐색 종료
        if count == k or len(curr) == n:
            continue
        for pipe_type in [1, 2, 3]:
            next_set = infect(curr, pipe_type)
            
            # 새로 감염된 배양체가 생겼을 경우에만 다음 단계 탐색 진행
            if len(next_set) > len(curr):
                new_state = tuple(sorted(list(next_set)))
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((next_set, count + 1))
                
    return maximum