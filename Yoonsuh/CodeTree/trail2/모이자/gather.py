n = int(input())
A = list(map(int, input().split()))
minv = float('inf')
for j in range(n):
    sumv = 0
    distance = [0] * n
    distance[j] = 0
    for i in range(0, j):
        distance[i] = abs(j - i)

    for i in range(j+1, n):
        distance[i] = abs(i - j)
    for k in range(n):
        sumv += A[k] * distance[k]
    minv = min(minv, sumv)

print(minv)

    