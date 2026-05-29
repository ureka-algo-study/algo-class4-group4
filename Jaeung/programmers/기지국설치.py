# 처음 풀이에서는 전파가 도달하지 않는 아파트들을 리스트에 따로 저장, 값들을 비교하는 방식으로 알고리즘을 작성하였다.
# range(1, N+1)로 전체 아파트 리스트를 만들면 N 값이 큰 경우 사용 메모리와 실행 시간이 너무 커져 효율성 테스트 실패(시간 초과)가 나왔다.
# 리스트 사용 없이 기지국 사이에 전파가 도달하지 않는 공간의 거리만을 계산하는 풀이

import math

def solution(N, stations, W):
    answer = 0
    W_range = 2 * W + 1
    # 현재 전파가 도달하는지 확인하는 아파트 위치
    curr_idx = 1

    for s in stations:
        # 기지국 s의 전파 시작 지점(s - W)이 현재 아파트 위치(curr_idx)보다 큰 경우, 그 사이의 아파트들에는 전파가 도달하지 않는다.
        if s - W > curr_idx:
            # length : 전파가 도달하지 않는 아파트 공간의 거리 / 추가적으로 증설해야 할 기지국의 개수를 올림하여 answer에 추가한다.
            length = (s - W) - curr_idx
            answer += math.ceil(length / W_range)
        # 현재 아파트 위치를 기지국 s의 전파가 끝나는 지점(s + W)의 다음 위치(s + W + 1)로 갱신한다.
        curr_idx = s + W + 1

    # stations의 마지막 기지국 탐색 이후 남아있는 아파트들에 대하여, 추가적으로 증설해야 할 기지국의 개수를 올림하여 answer에 추가한다.
    if curr_idx <= N:
        length = N - curr_idx + 1
        answer += math.ceil(length / W_range)

    return answer