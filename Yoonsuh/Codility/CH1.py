##### factorial #####
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(factorial)

##### 중첩 for문 - 별 삼각형 #####
n = 4
for i in range(1, n+1):
    for j in range(i):
        print('*', end= ' ')
    print()

##### range #####
for i in range(10, 0, -1):
    print(i)

##### 피보나치 수열 while #####
n = 100
a = 0
b = 1

while a <= n:
    print(a)
    c = a + b
    a = b
    b = c

##### 리스트 순회 #####
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']
for day in days:
    print(day)
print()
##### 집합 set으로 순회는 순서 보장이 없어서 실행할 때마다 결과 달라짐 #####
days = set(['Monday', 'Tuesday', 'Wednesday'])

for day in days:
    print(day)

##### 딕셔너리 순회 - key를 순회 #####
days = {'mon': 'Monday', 'tue': 'Tuesday', 'wed': 'Wednesday'}

for day in days: ##### key만 나오므로 value는 days[day]
    print(day)

##### 딕셔너리 카운팅 #####
from collections import Counter
s = "LILLYBILLYBOO"
cnt = Counter(s)
print(cnt)