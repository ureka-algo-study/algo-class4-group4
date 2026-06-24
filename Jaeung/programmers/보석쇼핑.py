def solution(gems):
    gem_size = len(set(gems))
    gem_count = {}
    left = 0
    answer = (0, len(gems) - 1)

    for right, gem in enumerate(gems):
        # gem 값이 처음 나오면 1로 초기화, 이미 있으면 count +1
        gem_count[gem] = gem_count.get(gem, 0) + 1
        
        while len(gem_count) == gem_size:
            # 현재 구간이 지금까지 찾은 최소 구간보다 길이가 짧을 때만 answer를 갱신한다.
            if right - left < answer[1] - answer[0]:
                answer = (left, right)
                
            # left 포인터를 오른쪽으로 한 칸 이동하며 구간을 좁힌다.
            left_gem = gems[left]            
            gem_count[left_gem] -= 1
            # count가 0이 되면 해당 보석이 구간에서 사라진 것이므로 딕셔너리에서 삭제한다.
            if gem_count[left_gem] == 0:
                del gem_count[left_gem]
            left += 1

    # 진열대 번호가 1부터 시작하므로 1씩 더해준다.
    return [answer[0] + 1, answer[1] + 1]