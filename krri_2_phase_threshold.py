# import h5py
# import os
# import numpy as np
# import pandas as pd
# import dask.array as da
# import scipy.signal as signal
# import random
#
# # 설정 변수
# fs = 2500  # 샘플링 주파수 (2500 Hz)
# cutoff = 4  # 하이패스 필터 컷오프 주파수
# nyq = 0.5 * fs  # 나이퀴스트 주파수
# b, a = signal.butter(5, cutoff / nyq, btype='high', analog=False)
# duration_in_seconds = 1  # 데이터 수집 기간 (1초)
# num_samples = duration_in_seconds * fs  # 1초 동안의 샘플 수 (2500)
#
# # HDF5 파일이 있는 디렉토리 경로
# directory = r'F:\240821_osong_hdf5\240709_10'
#
# # 디렉토리 내 .hdf5 파일 리스트 생성
# hdf5_files = [file for file in os.listdir(directory) if file.endswith('.hdf5')]
#
# # 파일이 51개보다 적을 경우, 모든 파일을 사용하도록 설정
# num_files_to_sample = min(51, len(hdf5_files))
# sampled_files = random.sample(hdf5_files, num_files_to_sample)
#
# # 모든 파일에 대해 절대값 합계 데이터를 저장할 배열 초기화
# all_sum_data_phase_filtered = []
#
# # 각 파일에 대해 반복
# for file_name in sampled_files:
#     file_path = os.path.join(directory, file_name)
#
#     with h5py.File(file_path, 'r', libver='latest') as h5_file:
#         # 데이터 크기 가져오기
#         total_samples = h5_file['/DAS'].shape[1]  # 전체 샘플 수
#
#         # 랜덤한 시작 위치 선택
#         start_idx = random.randint(0, total_samples - num_samples)
#         end_idx = start_idx + num_samples
#
#         # 랜덤 구간의 데이터 추출
#         T_data = h5_file['/DAS'][start_idx:end_idx, :]
#
#         # Dask 배열로 변환 및 누적 합 계산
#         T_darr = da.from_array(T_data, chunks=(num_samples, T_data.shape[1]))
#         T_phase = T_darr.cumsum(axis=0).compute()
#         T_phase = T_phase * (np.pi / 2 ** 15)
#
#         # 필터 적용
#         T_data_phase_filtered = signal.filtfilt(b, a, T_phase, axis=0)
#
#         # 각 위치별 절대값의 합계 계산
#         sum_data_phase_filtered = np.sum(np.abs(T_data_phase_filtered), axis=0)
#
#         # 모든 파일의 데이터를 누적
#         all_sum_data_phase_filtered.append(sum_data_phase_filtered)
#
# # 리스트를 numpy 배열로 변환
# all_sum_data_phase_filtered = np.array(all_sum_data_phase_filtered)
#
# # 각 위치에 대해 평균값과 표준편차 계산
# mean_values = np.mean(all_sum_data_phase_filtered, axis=0)
# std_values = np.std(all_sum_data_phase_filtered, axis=0)
#
# # Threshold 계산
# threshold = mean_values + (3 * std_values)
#
# # 결과를 데이터프레임으로 변환
# df = pd.DataFrame({
#     'Position': np.arange(len(threshold)),
#     'Threshold': threshold
# })
#
# # CSV 파일로 저장
# output_csv = r'C:\Users\MSI\project\DAS\krri\threshold_results_3.csv'
# df.to_csv(output_csv, index=False)
#
# print(f"CSV 파일이 저장되었습니다: {output_csv}")

import h5py
import os
import numpy as np
import pandas as pd
import dask.array as da
import scipy.signal as signal
import random

# 설정 변수
fs = 2500  # 샘플링 주파수 (2500 Hz)
cutoff = 4  # 하이패스 필터 컷오프 주파수
nyq = 0.5 * fs  # 나이퀴스트 주파수
b, a = signal.butter(5, cutoff / nyq, btype='high', analog=False)
duration_in_seconds = 1  # 데이터 수집 기간 (1초)
num_samples = duration_in_seconds * fs  # 1초 동안의 샘플 수 (2500)

# HDF5 파일이 있는 최상위 디렉토리 경로
base_directory = r'F:\240821_osong_hdf5'

# 모든 하위 디렉토리를 포함하여 .hdf5 파일 리스트 생성
hdf5_files = []
for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file.endswith('.hdf5'):
            hdf5_files.append(os.path.join(root, file))

# 파일이 51개보다 적을 경우, 모든 파일을 사용하도록 설정
num_files_to_sample = min(51, len(hdf5_files))
sampled_files = random.sample(hdf5_files, num_files_to_sample)

# 모든 파일에 대해 절대값 합계 데이터를 저장할 배열 초기화
all_sum_data_phase_filtered = []

# 각 파일에 대해 반복
for file_path in sampled_files:
    with h5py.File(file_path, 'r', libver='latest') as h5_file:
        # 데이터 크기 가져오기
        total_samples = h5_file['/DAS'].shape[1]  # 전체 샘플 수

        # 랜덤한 시작 위치 선택
        start_idx = random.randint(0, total_samples - num_samples)
        end_idx = start_idx + num_samples

        # 랜덤 구간의 데이터 추출
        T_data = h5_file['/DAS'][start_idx:end_idx, :]

        # Dask 배열로 변환 및 누적 합 계산
        T_darr = da.from_array(T_data, chunks=(num_samples, T_data.shape[1]))
        T_phase = T_darr.cumsum(axis=0).compute()
        T_phase = T_phase * (np.pi / 2 ** 15)

        # 필터 적용
        T_data_phase_filtered = signal.filtfilt(b, a, T_phase, axis=0)

        # 각 위치별 절대값의 합계 계산
        sum_data_phase_filtered = np.sum(np.abs(T_data_phase_filtered), axis=0)

        # 모든 파일의 데이터를 누적
        all_sum_data_phase_filtered.append(sum_data_phase_filtered)

# 리스트를 numpy 배열로 변환
all_sum_data_phase_filtered = np.array(all_sum_data_phase_filtered)

# 각 위치에 대해 평균값과 표준편차 계산
mean_values = np.mean(all_sum_data_phase_filtered, axis=0)
std_values = np.std(all_sum_data_phase_filtered, axis=0)

# Threshold 계산
threshold = mean_values + (3 * std_values)

# 결과를 데이터프레임으로 변환
df = pd.DataFrame({
    'Position': np.arange(len(threshold)),
    'Threshold': threshold
})

# CSV 파일로 저장
output_csv = r'C:\Users\MSI\Desktop\company\develop\DAS\KRRI\threshold_results_3.csv'
df.to_csv(output_csv, index=False)

print(f"CSV 파일이 저장되었습니다: {output_csv}")
