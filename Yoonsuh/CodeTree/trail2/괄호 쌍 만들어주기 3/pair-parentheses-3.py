A = input()
n = len(A)
count = 0
for j in range(n):
    if A[j] == '(':
        for i in range(j, n):
            if A[i] == ')':
                count+=1

print(count)