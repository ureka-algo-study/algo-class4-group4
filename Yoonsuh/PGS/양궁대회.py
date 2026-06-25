from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    # 1. 아이디어: n발의 화살을 0~10번 과녁에 중복조합으로 배분하는 모든 경우를 탐색.
    #    combinations_with_replacement(range(11), n) → 11개 과녁 중 n개를 중복 허용해서 고르기.
    #    점수 계산 후 라이언이 이기는 경우 중 최대 점수 차를 갱신.
    # 2. 시간복잡도: O(C(11+n-1, n) * 11) → n=10 기준 약 20C10 * 11 ≈ 18만, 통과 가능
    # 3. 자료구조: Counter(조합→과녁별 화살 수), 리스트(배분 결과)

    answer = [-1]
    info = info[::-1]  # 인덱스 i => i점 과녁으로 맞추기 위해 역순 정렬
                       # 원래 info[0]=10점, info[10]=0점 → 역순하면 info[0]=0점, info[10]=10점
        
    lenv = len(info)   # 11
    maxv = -1

    for c in combinations_with_replacement(range(11), n): # 중복조합 기반으로 반복하며 정답 도출
        # n=5일 때 (0, 0, 2, 3, 10) → 0점 과녁 2번, 2점 1번, 3점 1번, 10점 1번
        ryan = 0
        apeach = 0
        tmp_answer = [0] * lenv # 상황별 배분 기록을 유동적으로 변경하며 저장

        c = Counter(c)  # {과녁번호: 화살수} 딕셔너리로 변환
                        # Counter({0: 2, 2: 1, 3: 1, 10: 1})

        for i in range(lenv):
            # i = 과녁 점수 (역순 정렬 후이므로 인덱스 = 점수)
            if info[i] < c[i]:       # 라이언이 어피치보다 많이 쐈으면
                ryan += i            # 라이언이 i점 획득
            elif info[i] != 0:       # 어피치가 1발이라도 쐈고 라이언이 못 가져가면
                apeach += i          # 어피치가 i점 획득
            tmp_answer[i] = c[i]     # 현재 배분 기록

        if ryan > apeach:            # 라이언이 이기는 경우만
            diff = ryan - apeach
            if maxv < diff:          # 더 큰 점수 차이면 갱신
                maxv = diff
                answer = tmp_answer

    if answer:
        return answer[::-1]  # 역순으로 돌려서 원래 형식(10점~0점)으로 반환

    return answer