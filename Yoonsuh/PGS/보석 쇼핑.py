def solution(gems):
    answer = [1, 100000] # 최대 크기 상태로 선언
    gem_dict = dict() # 딕셔너리 형태로 gem 값 : 인덱스+1 위치 형태로 저장
    unique_num = len(set(gems)) # 고유한 gem들의 개수
    start, end = 1, len(gems) # gems 배열 기준 처음과 끝 위치 초기화
    
    for i, gem in enumerate(gems):
        gem_dict[gem] = i + 1 
        if gem == gems[start-1]:
            start = min(gem_dict.values())
        
        if len(gem_dict) == unique_num:
            end = i + 1 
            if end - start < answer[1] - answer[0]: # 구간 크기가 더 작으면 대체
                answer = [start, end]
                
    return answer