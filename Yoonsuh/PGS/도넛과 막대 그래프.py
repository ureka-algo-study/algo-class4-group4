def solution(edges):
    answer = [0, 0, 0, 0] # 생성 정점, 도넛, 막대, 8자
    max_val = max(map(max, edges)) + 1  # +1로 인덱스 맞추기
    in_cnt, out_cnt = [0] * max_val, [0] * max_val
        
    # in, out 간선 저장
    for now_out, now_in in edges:
        out_cnt[now_out] += 1
        in_cnt[now_in] += 1
        
    for now_node in range(1, max_val):
        if in_cnt[now_node] == 0 and out_cnt[now_node] >= 2: # 생성 노드
            answer[0] = now_node 
        elif in_cnt[now_node] >= 1 and out_cnt[now_node] == 0: # 막대 그래프
            answer[2] += 1
        elif in_cnt[now_node] >= 2 and out_cnt[now_node] == 2: # 8자 그래프 
            answer[3] += 1
    answer[1] = out_cnt[answer[0]] - sum(answer[2:])    # 도넛 그래프
    
    return answer