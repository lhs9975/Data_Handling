# import pandas as pd
# import os
# import re
#
# # 파일명에서 숫자 추출 함수
# def extract_number(filename):
#     numbers = re.findall(r'\d+', filename)
#     return int(numbers[0]) if numbers else float('inf')  # 숫자가 없으면 무한대 반환
#
# # CSV 파일들이 있는 디렉토리 경로 설정
# directory_path = r"C:\Users\MSI\Desktop\company\develop\DAS\Train_Torch\log"
#
# # 디렉토리 내 모든 CSV 파일 목록 가져오기 및 숫자 기반으로 정렬
# csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
# csv_files = sorted(csv_files, key=extract_number)  # 파일명에서 숫자를 추출해 정렬
#
# # CSV 파일 전체 경로로 변환
# file_paths = [os.path.join(directory_path, file) for file in csv_files]
#
# # 모든 CSV 파일 불러오기
# dataframes = [pd.read_csv(file) for file in file_paths]
#
# # 첫 번째 파일에서 시간 열 추출
# time_column = dataframes[0]['Unnamed: 0']
#
# # 각 데이터프레임에서 시간 열 제거
# for df in dataframes:
#     df.drop(columns='Unnamed: 0', inplace=True)
#
# # 시간 열과 나머지 위치 열들을 가로로 결합
# combined_data = pd.concat([time_column] + dataframes, axis=1)
#
# # 결합된 데이터를 CSV 파일로 저장 (원하는 파일명으로 변경 가능)
# output_file_path = os.path.join(directory_path, "combined_data.csv")
# combined_data.to_csv(output_file_path, index=False)
#
# # 결합된 데이터 출력
# print(combined_data)



import matplotlib.pyplot as plt
import pandas as pd

# CSV 파일 불러오기
file_path = r"C:\Users\MSI\Desktop\company\develop\DAS\Train_Torch\log\threshold_over_classification_0.csv"
data = pd.read_csv(file_path)

# 데이터를 'hot' 컬러맵과 주어진 인자들로 플롯, 0과 1에 대한 명확한 대비를 위해 vmin과 vmax 설정
plt.imshow(data, cmap='hot', interpolation='nearest', aspect='auto', origin='lower', vmin=0, vmax=1)

# 그래프 보여주기
plt.show()
