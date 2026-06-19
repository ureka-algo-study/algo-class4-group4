def solution(stones, k):
    left = 0
    right = 200000000
    while left <= right:
        temp_stones = stones.copy()  # mid 값마다 새로 검사해야 하므로 원본 보존용 복사
        mid = (left + right) // 2    # 현재 시도해볼 건너는 사람 수(가설)
        cnt = 0  # 연속으로 못 밟는(내구도 부족) 돌의 개수

        for stone in temp_stones:
            if stone - mid <= 0:
                # mid명이 밟으면 내구도가 0 이하가 되는 돌 -> 못 밟는 돌
                cnt += 1
            else:
                # 밟을 수 있는 돌이 나오면 연속 카운트 끊김
                cnt = 0
            if cnt >= k:
                # 못 밟는 돌이 k개 연속되면 그 즉시 건너기 실패 확정
                break

        if cnt >= k:
            # mid명은 건너지 못함 -> 더 적은 인원으로 다시 시도 (가능 범위를 왼쪽으로 좁힘)
            right = mid - 1
        else:
            # mid명은 건널 수 있음 -> 더 많은 인원도 가능한지 확인 (오른쪽으로 좁힘)
            left = mid + 1

    # 탐색이 끝나면 left가 "건널 수 있는 최대 인원 수"가 됨
    return left