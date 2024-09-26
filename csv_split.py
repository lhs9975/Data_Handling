import pandas as pd
import os

# CSV 파일 경로 설정
input_file = r"C:\Users\MSI\Desktop\company\develop\DTS\MLTA_Gwangyang\data\POSCO_0717-0925_0_640\POSCO_0717-0925_0_640.csv"
output_directory = r"C:\Users\MSI\Desktop\company\develop\DTS\MLTA_Gwangyang\POSCO_0717-0925_0_640"  # 출력 디렉터리 지정
output_file_prefix = 'POSCO_0717-0925_0_466'  # 출력될 파일의 접두사
chunk_size = 40000  # 40,000행씩 분할

# 출력 디렉터리가 없으면 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# CSV 파일을 chunk 단위로 읽어서 각 파일로 저장
for i, chunk in enumerate(pd.read_csv(input_file, chunksize=chunk_size)):
    # 출력 파일 경로 설정
    output_file = os.path.join(output_directory, f'{output_file_prefix}_{i + 1}.csv')

    # 분할된 CSV 파일 저장
    chunk.to_csv(output_file, index=False)
    print(f'저장된 파일: {output_file}')
