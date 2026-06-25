arr = [0, 6, 3, 2, 4, 9, 1]
k = 10
n = 6

# 가능한 구간 중 최대 크기를 구합니다.
ans = 0

# 모든 구간을 탐색합니다.
for i in range(1, n + 1):
    for j in range(i, n + 1):
        # 구간 내 합을 구합니다.
        sum_val = 0
        for l in range(i, j + 1):
            sum_val += arr[l]

        # 구간 내 합이 10 이하라면,
        # 구간 크기 중 최댓값을 갱신합니다.
        if sum_val <= k:
            ans = max(ans, j - i + 1)
    
# 조건을 만족하는 가장 큰 구간의 크기는
# [3, 2, 4]로 3이 됩니다.
print(ans)
