def solution(gems):
    # 1. 아이디어: 각 보석의 가장 최근 등장 위치를 딕셔너리에 갱신하며 오른쪽(end)을 전진.
    #    모든 종류가 모이면(len(gem_dict)==unique_num) start=min(values())로 구간 왼쪽 계산.
    #    단, start 갱신은 현재 gem이 start 위치 보석과 같을 때만 수행 → 일부 케이스 누락 버그 존재.
    #    정석 투 포인터(left를 직접 한 칸씩 이동)와 달리 min(values())로 start를 계산 → O(N*K).
    # 2. 시간복잡도: O(N*K) - N: gems 길이, K: 보석 종류 수 (정석은 O(N))
    # 3. 자료구조: dict(보석별 최근 위치 관리), set(고유 보석 수 계산)

    answer = [1, 100000]        # 초기값: 최대 구간 크기로 선언 (이후 갱신)
    gem_dict = dict()           # {보석명: 가장 최근 인덱스+1 위치}
    unique_num = len(set(gems)) # 고유 보석 종류 수 (모든 종류가 모였는지 기준)
    start, end = 1, len(gems)   # 1-indexed 기준 구간 초기화

    for i, gem in enumerate(gems):
        gem_dict[gem] = i + 1   # 현재 보석의 최근 위치를 갱신 (1-indexed)

        if gem == gems[start-1]:
            # 현재 추가한 보석이 start 위치 보석과 같을 때만 start 재계산
            # → start 위치 보석의 등장이 오른쪽으로 밀렸으니 min으로 새 start 탐색
            # 버그: 다른 보석의 위치가 갱신돼 min이 바뀌는 경우는 처리 못 함
            start = min(gem_dict.values())  # O(K) - 매 반복마다 전체 순회

        if len(gem_dict) == unique_num:     # 모든 종류의 보석이 구간 안에 존재
            end = i + 1                     # 현재 오른쪽 끝 위치 (1-indexed)
            if end - start < answer[1] - answer[0]:  # 더 짧은 구간이면 갱신
                answer = [start, end]

    return answer