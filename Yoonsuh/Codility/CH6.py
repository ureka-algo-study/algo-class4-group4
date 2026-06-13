##### Sorting 강의 #####
# 1. 기본 정렬
A = [5, 2, 8, 1, 9, 3]
A.sort()
print(A)   # [1, 2, 3, 5, 8, 9]

# 2. 고유값 개수
print(len(set([1,1,2,3,3,4])))   # 4

# 3. 정렬 후 인접 비교
def distinct(A):
    if not A:
        return 0
    A.sort()
    rs = 1
    for k in range(1, len(A)):
        if A[k] != A[k-1]:
            rs += 1
    return rs

print(distinct([2,1,1,2,3,1]))   # 3
print(distinct([]))               # 0

# 4. 복합 정렬
students = [('Alice', 90), ('Bob', 85), ('Charlie', 90)]
students.sort(key=lambda x: (-x[1], x[0]))
print(students)   # [('Alice', 90), ('Charlie', 90), ('Bob', 85)]