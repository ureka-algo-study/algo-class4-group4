from collections import Counter

A = [2, 3, 2, 5, 3, 2]
m = 5
count = [0] * (m+1)
for x in A:
    count[x] += 1
print(count)

cnt = Counter(A)
print(cnt.most_common(1))

def fast_solution(A, B, m):
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a

    if d % 2 == 1:
        return False
    d //= 2

    count = [0] * (m+1)
    for a in A:
        count[a] += 1
    for b in B:
        target = b - d
        if 0 <= target <= m and count[target] > 0:
            return True
    return False

# 3. swap 문제
print(fast_solution([1,2,3], [3,2,5], 5))   # True
print(fast_solution([1,2], [3,5], 5))        # False