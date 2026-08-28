import numpy as np
import pandas as pd

# 1. CSV 읽기
data = pd.read_csv(path)

# 2. 열 통계
data['col'].min() / .max() / .mean() / .sum()

# 3. 조건 필터링
data[data['col'] > 값]
data[data['col'] == '문자열']

# 4. 조건 개수 세기
(data['col'] == 'YES').sum()

# 5. 새 열 계산해서 추가
data['new'] = (data['x'] - tx) ** 2

# 6. 열 정규화
data['x'] = (data['x'] - data['x'].min()) / (data['x'].max() - data['x'].min())

# 7. 정렬
data = data.sort_values('col')

# 8. 위치 기반 접근
data.iloc[k-1]['col']

# 9. 행 값 배열로 추출
data.values[0]  # 첫 번째 행

# 10. numpy 배열 생성 및 셔플
arr = np.array([1]*n + [0]*m)
rng = np.random.default_rng(seed)
rng.permutation(arr)

"""
DataFrame  → 엑셀 표, 행=데이터, 열=피처
열 선택    → data['col']
기본 통계  → .min() .max() .mean() .sum()
필터링     → data[조건]
값 개수    → (조건).sum()
열 수정    → data['col'] = 수식
정렬       → sort_values('col')
iloc       → 위치 기반, 정렬 후 반드시 iloc
values     → DataFrame → numpy 배열
numpy seed → 재현 가능한 랜덤
"""