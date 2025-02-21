import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 1. CSV 불러오기
df = pd.read_csv(r"C:\Users\MSI\Desktop\company\develop\DTS\GS_ENR\Data\test_data\5_hour_GS_ENR_2024_06_19.csv")

# 2. 'date_time' 제외한 나머지 열 이름(거리: 0, 0.25, 0.5, ...) 가져오기
distance_cols = df.columns[1:]

# 3. 전체 데이터 중 최고 온도를 갖는 행 찾기
row_with_max = df[distance_cols].max(axis=1).idxmax()

# 4. 최고 온도를 갖는 행의 날짜
max_date = df.loc[row_with_max, 'date_time']

# 5. x, y값 준비
y_values = df.loc[row_with_max, distance_cols].values
x_values = [float(dist) for dist in distance_cols]

# ==========
#   한글 폰트 설정
# ==========
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 6. x축 범위와 눈금 설정 (필요시)
x_min, x_max = 35, 105
xticks = np.arange(x_min, x_max+0.1, 5)

# 7. 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, linestyle='-', label='온도 곡선')

plt.title(f"5시 방향 최고기온 날짜: {max_date}")
plt.xlabel("거리")
plt.ylabel("온도")

plt.xticks(xticks)
plt.xlim(x_min, x_max)
plt.ylim(20, 100)
plt.grid(True)
plt.tight_layout()

# -------------------------------------------
# (A) 그래프 상 최대 온도 지점에 마커 표시
# -------------------------------------------
# y_values 중 최댓값과 그 인덱스
max_temp_idx = np.argmax(y_values)
max_temp = y_values[max_temp_idx]
max_dist = x_values[max_temp_idx]

# 1) 점(마커) 표시
plt.plot(max_dist, max_temp, marker='o', color='red', markersize=8, label='최고 온도 지점')

# 2) 텍스트 표시 (간단한 방법)
#   - (max_dist+1, max_temp) 같은 식으로 xytext를 약간 옆에 두면 겹치지 않게 됨
plt.annotate(
    f'{max_temp:.2f}°C',       # 표시할 텍스트(소수점 2자리)
    xy=(max_dist, max_temp),   # 화살표가 가리킬 좌표
    xytext=(max_dist+1, max_temp+2),  # 텍스트를 배치할 좌표 (약간 띄워서)
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=10,
    color='red'
)

plt.legend()  # 범례 표시

plt.show()
