from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        counter = Counter()
        for order in orders:
            # 주문을 알파벳 순서대로 미리 정렬해 (A,B) 조합과 (B,A) 조합이 다르게 인식되는 것을 방지한다.
            sorted_order = sorted(order)
            # 정렬된 order에서 개수가 c인 조합을 모두 생성해 counter에 추가한다.
            for combo in combinations(sorted_order, c):
                counter[combo] += 1
        
        # 코스 길이가 c인 조합에서 가장 많이 등장한 횟수를 구한다. 
        max_count = max(counter.values())  
        # 최소 2명 이상이 주문한 조합만 코스요리 메뉴로 선정한다는 조건 반영 
        # (max_count = 1이면 조합이 겹치지 않은 것이므로 반영 X)
        if max_count >= 2:
            for combo, count in counter.items():
                # counter를 순회하면서 최댓값(max_count)과 동일한 횟수인 조합만 answer에 추가한다.
                # (가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성)
                if count == max_count:
                    answer.append("".join(combo))
    
    # 사전 순으로 오름차순 정렬
    answer = sorted(answer) 
    return answer
