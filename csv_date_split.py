import os
import pandas as pd

# CSV 파일 읽기
df = pd.read_csv(r"C:\Users\MSI\Desktop\company\develop\DTS\MLTA_LIVE_Gunsan\data\2024_09_2024_10\Gunsan_2024_09_2024_10.csv")

# date_time 열을 datetime 형식으로 변환
df['date_time'] = pd.to_datetime(df['date_time'])

# 날짜만 추출해서 새로운 열 'date' 생성
df['date'] = df['date_time'].dt.date

# 저장할 디렉터리 경로 지정
output_dir = r"C:\Users\MSI\Desktop\company\develop\DTS\MLTA_LIVE_Gunsan\data\2024_09_2024_10"
os.makedirs(output_dir, exist_ok=True)  # 디렉터리가 없으면 생성

# 날짜별로 그룹핑하여 CSV 파일 분리 저장
for date_value, group_df in df.groupby('date'):
    # 예: '2024-11-01.csv' 식으로 파일명 생성
    output_filename = f'{date_value}.csv'
    # 지정한 폴더 경로 + 파일명으로 저장 경로 구성
    output_path = os.path.join(output_dir, output_filename)
    group_df.to_csv(output_path, index=False)

print("일별로 CSV 파일이 저장되었습니다!")
