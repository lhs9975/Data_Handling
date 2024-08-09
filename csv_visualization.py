# import pandas as pd
# import matplotlib.pyplot as plt
#
# # CSV 파일 불러오기 (파일 경로를 적절히 변경하세요)
# file_path = r"C:\Users\MSI\Desktop\company\develop\DTS\MLTA\DB_Connect\data\GS_ENR_0.25\test02.csv"
#
# # CSV 파일을 데이터프레임으로 불러오기
# df = pd.read_csv(file_path)
#
# # 첫 번째 열을 시간으로 설정하고, 나머지 열은 위치별 온도
# df['시간'] = pd.to_datetime(df['시간'])
# df.set_index('시간', inplace=True)
#
# # 특정 위치의 온도를 시간에 따라 플로팅
# position = '35'  # 원하는 위치 값으로 변경 가능
# plt.figure(figsize=(10, 5))
# plt.plot(df.index, df[position], marker='o')
# plt.title(f'위치 {position}의 시간에 따른 온도 변화')
# plt.xlabel('시간')
# plt.ylabel('온도')
# plt.grid(True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm

# CSV 파일 불러오기 (파일 경로를 적절히 변경하세요)
file_path = r"C:\Users\MSI\Desktop\company\develop\DTS\MLTA\DB_Connect\data\GS_ENR_0.25\test.csv"

# 첫 번째 열을 인덱스로 설정하고 데이터프레임으로 불러오기
df = pd.read_csv(file_path)

# 'date_time' 열을 datetime 형식으로 변환 (형식 자동 감지)
df['date_time'] = pd.to_datetime(df['date_time'])

# 'date_time' 열을 인덱스로 설정
df.set_index('date_time', inplace=True)

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 윈도우에서 기본 제공하는 한글 폰트 경로
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 특정 위치의 온도를 시간에 따라 플로팅
position = '73'  # 원하는 위치 값으로 변경 가능
plt.figure(figsize=(10, 5))
plt.plot(df.index, df[position])

# x축에 초 단위까지 표시되도록 설정
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.SecondLocator(interval=60))  # 10초 간격으로 표시

# x축의 범위를 데이터의 최소값과 최대값으로 설정하여 빈 공간 제거
plt.xlim(df.index.min(), df.index.max())
plt.ylim(25, 45)

plt.title(f'6월 20일 09:36:04 ~ 10:10:54 {position}m 시간에 따른 온도 변화')
plt.xlabel('시간')
plt.ylabel('온도')
plt.grid(True)
plt.xticks(rotation=45)  # x축 라벨이 겹치지 않도록 회전

plt.tight_layout()

plt.show()
