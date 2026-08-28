### 그리디 ###
"""
1. 핵심 개념
    "지금 이 순간 가장 좋아 보이는 선택을 반복한다"
미래를 고려하지 않고 현재 상황에서 최선의 선택을 계속 해나가는 방식. 단,
그리디가 성립하려면 조건이 있다.
매 순간의 최선이 전체의 최선이 되어야 한다.
이게 되어야 그리디. 안되면 DP나 완전탐색

2. 그리디 문제 풀이 공식
1. 정렬 기준을 찾는다
2. 그 기준대로 정렬한다
3. 앞 또는 뒤에서부터 탐욕적으로 선택한다.
4. 반례가 없는지 검증한다.
"""

### 3. 그리디 유형 분류 ###
# 3-1. 정렬 후 순서대로 탐욕적 선택
# def solution(n, lost, reserve):
#     real_lost = set(lost) - set(reserve)
#     real_reserve = set(reserve) - set(lost)

#     for r in sorted(real_reserve):
#         if r-1 in real_lost:
#             real_lost.remove(r-1)
#         elif r+1 in real_lost:
#             real_lost.remove(r+1)

#     return n - len(real_lost)

# 3-2. 투포인터 기반 그리디
# 핵심: 양 끝에서 좁혀오며 최적 쌍 선택

# def solutions(people, limit):
#     people.sort()
#     left, right = 0, len(people) - 1
#     answer = 0
#     while left <= right:
#         if people[left] + people[right] <= limit:
#             left += 1
#         right -= 1
#         answer += 1
    
#     return answer

# 3-3. 구간/범위 기반 그리디
# 핵심: 끝나는 시간 기준 정렬 후 겹치지 않게 선택
def solution(meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))
    answer = 0
    end = 0
    for start, finish in meetings:
        if start >= end:
            answer += 1
            end = finish
    return answer

# 3-4. 누적/시뮬레이션 기반 그리디
# 핵심: 오른쪽 혹은 왼쪽 끝부터 처리하며 필요한 만큼 소비

def solution(number, k):
    stack = []
    for n in number:
        while k < 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)

