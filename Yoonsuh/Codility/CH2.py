##### 배열 #####

### 초기값으로 채우기 ###
temperatures = [0] * 365

### 원소 추가 ###
shopping = ['bread', 'butter', 'cheese']
shopping += ['eggs']

### 인덱스와 값이 둘 다 필요시 ###
arr = ['a', 'b', 'c']
for i, item in enumerate(arr):
    print(i, item)

### 배열 뒤집기 ###
A = [1, 2, 3, 4, 5]
def reverse(A):
    N = len(A)
    for i in range(N // 2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    return A

A.reverse
B = A[::-1]

### 코테 관점 ###
arr = [10, 20, 30, 40, 50]
print(arr[1:4])
print(arr[::-1])
print(arr[-1])

print(30 in arr)
print(99 in arr)

for i, v in enumerate(arr):
    print(f"{i}: {v}")