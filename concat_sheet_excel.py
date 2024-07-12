# excel sheet 결합 코드

import os
import pandas as pd

# 디렉터리 경로 지정
directory = r"C:\Users\MSI\Desktop\회사\개발\GS_ENR\Data\csv"

# 빈 DataFrame 생성
all_temp_data = pd.DataFrame()

# 디렉터리 내의 모든 파일에 대해 반복
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):  # Excel 파일만 선택
        # Excel 파일 불러오기
        filepath = os.path.join(directory, filename)
        data = pd.read_excel(filepath, sheet_name=None, engine='openpyxl')

        # 각 시트에서 온도 데이터만 선택
        temp_data_per_file = pd.DataFrame()
        for sheet_name, df in data.items():
            temp_data = df.iloc[1:1000, 1]  # 1열(온도 데이터)만 선택
            temp_data_per_file = pd.concat([temp_data_per_file, temp_data], axis=1)

        # 모든 파일의 데이터를 하나로 연결
        all_temp_data = pd.concat([all_temp_data, temp_data_per_file], axis=1)

# 모든 데이터를 하나의 Excel 파일로 저장
output_filepath = r"C:\Users\MSI\Desktop\회사\개발\GS_ENR\Data\all_data\CH2\GS_ENR_CH2_PM.xlsx"
all_temp_data.to_excel(output_filepath, index=False, header=False)

print("The data from all Excel files in the folder have been concatenated and saved as:", output_filepath)
