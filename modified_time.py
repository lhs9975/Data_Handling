import os
import pandas as pd
from datetime import datetime

# 파일 경로 설정
directory = r'C:\Users\MSI\Desktop\회사\개발\GS_ENR\Data\tra\ch2\5월 31일_6월 3일\all2'

# 파일 목록 가져오기
files = os.listdir(directory)

# 파일 정보 저장할 리스트 생성
file_data = []

# 각 파일의 수정 날짜 가져오기
for file in files:
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
        modified_time = os.path.getmtime(file_path)
        modified_date = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
        file_data.append([file, modified_date])

# 데이터프레임 생성
df = pd.DataFrame(file_data, columns=['File Name', 'Modified Date'])

# 엑셀 파일로 저장
excel_path = r'C:\Users\MSI\Desktop\회사\개발\GS_ENR\Data\tra\ch2\5월 31일_6월 3일\file_modification_dates.xlsx'
df.to_excel(excel_path, index=False)

print(f"파일의 수정 날짜가 '{excel_path}'에 저장되었습니다.")
