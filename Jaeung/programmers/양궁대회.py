def solution(n, info):
    
    info_ryan = [0] * 11
    answer = [-1] 
    max_diff = [0]
    
    def compare(info, info_ryan):
        sum_apeach, sum_ryan = 0, 0
        for i in range(len(info)):
            # 둘 다 0발을 맞혔을 경우, 둘 다 점수를 얻지 못한다.
            if info[i] == 0 and info_ryan[i] == 0: 
                continue
            if info[i] >= info_ryan[i]:
                sum_apeach += (10-i)
            else:
                sum_ryan += (10-i)
        
        return sum_ryan - sum_apeach
    
    
    def dfs(idx, remaining):     
        # idx: 현재 탐색 중인 과녁의 인덱스, remaining: 남은 화살 수
        
        # 모든 과녁 점수를 탐색 완료했으면 남은 화살은 전부 0점(idx = 10)에 배정한다.
        if idx == 10:
            info_ryan[10] = remaining
            
            diff = compare(info, info_ryan)
            if diff > max_diff[0]:
                max_diff[0] = diff
                answer[:] = info_ryan[:]  # 현재 상태를 복사해서 별도로 저장
            elif diff == max_diff[0] and diff > 0:
                # 점수 차가 같으면 더 낮은 점수 과녁을 많이 맞힌 배열로 갱신한다.
                for i in range(10, -1, -1):
                    if info_ryan[i] > answer[i]:
                        answer[:] = info_ryan[:]
                        break
                    elif info_ryan[i] < answer[i]:
                        break
                        
            info_ryan[10] = 0  # 다음 탐색 경로에 영향 주지 않도록 초기화
            return
        
        # 해당 과녁의 점수를 라이언이 얻는 경우 (어피치보다 1발 더 맞혀서)
        need = info[idx] + 1
        if remaining >= need:
            info_ryan[idx] = need
            dfs(idx + 1, remaining - need)
            info_ryan[idx] = 0
        
        # 해당 과녁의 점수를 포기하고 어피치가 얻는 경우
        dfs(idx + 1, remaining)
        
    dfs(0, n)
    return answer if max_diff[0] > 0 else [-1]