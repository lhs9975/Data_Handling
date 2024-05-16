# import os
# import pandas as pd
#
# # CSV 파일들이 저장된 디렉토리 경로
# directory = r'E:\MLTA_05_13_2'
#
# # 모든 파일의 온도 데이터를 저장할 리스트
# temperature_data = []
#
# # 디렉토리 내 모든 파일을 순회
# for filename in os.listdir(directory):
#     if filename.endswith(".csv"):
#         filepath = os.path.join(directory, filename)
#
#         # CSV 파일 읽기, 여러 인코딩 시도
#         encodings = ['utf-8', 'cp949', 'latin1', 'iso-8859-1']
#         for encoding in encodings:
#             try:
#                 df = pd.read_csv(filepath, encoding=encoding, errors='replace')
#                 break  # 성공적으로 읽으면 반복문 탈출
#             except UnicodeDecodeError:
#                 continue  # 다음 인코딩 시도
#
#         # 온도 열 추출 (스크린샷에 따르면 두 번째 열로 추정)
#         temperatures = df.iloc[:, 1].tolist()
#
#         # 온도 데이터를 리스트에 추가
#         temperature_data.extend(temperatures)
#
# # 수집된 온도 데이터로 DataFrame 생성
# temperature_df = pd.DataFrame(temperature_data, columns=['Temperature (°C)'])
#
# # 새로운 CSV 파일로 저장
# output_filepath = r'C:\Users\MSI\Desktop\회사\개발\MLTA\dataset\company_data\trace_data_excel\time_5\combined_temperatures.csv'
# temperature_df.to_csv(output_filepath, index=False)
#
# print(f"온도 데이터가 {output_filepath}에 저장되었습니다.")

import os
import pandas as pd

# CSV 파일들이 저장된 디렉토리 경로
directory = r'E:\MLTA_05_14_4'

# 모든 파일의 온도 데이터를 저장할 데이터프레임 리스트
data_frames = []

# 디렉토리 내 모든 파일을 순회
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)

        # CSV 파일 읽기, 여러 인코딩 시도
        encodings = ['utf-8', 'cp949', 'latin1', 'iso-8859-1']
        df = None
        for encoding in encodings:
            try:
                df = pd.read_csv(filepath, encoding=encoding)
                break  # 성공적으로 읽으면 반복문 탈출
            except (UnicodeDecodeError, pd.errors.ParserError):
                continue  # 다음 인코딩 시도

        if df is not None:
            # 온도 열 추출 (스크린샷에 따르면 두 번째 열로 추정)
            temperatures = df.iloc[3:, 1]

            # 데이터프레임으로 변환 후 리스트에 추가
            data_frames.append(temperatures)
        else:
            print(f"파일을 읽을 수 없습니다: {filename}")

# 모든 데이터프레임을 결합
combined_df = pd.concat(data_frames, axis=1)

# 새로운 CSV 파일로 저장
output_filepath = r'C:\Users\MSI\Desktop\회사\개발\MLTA\dataset\company_data\trace_data_excel\time_5\combined_temperatures_05_14_4.csv'
combined_df.to_csv(output_filepath, index=False, header=False)

print(f"온도 데이터가 {output_filepath}에 저장되었습니다.")

