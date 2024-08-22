# import h5py
# import numpy as np
# import scipy.signal
#
#
# file_name = r"C:\Users\MSI\project\DAS\krri\0000006155_2024-07-15_06.34.33.25722.hdf5"
#
# with h5py.File(file_name, 'r') as h5file:
#     fs = 2500
#     diff_phase = h5file['DAS'][:2500, 200]
#     phase_s64_T = np.int64(diff_phase)
#     data_phase = np.cumsum(phase_s64_T, axis=0) * (np.pi / 2**15)
#
# # Calulate the PSD using Scipy & Welch
# f, Pxx = scipy.signal.welch(data_phase, fs=fs, nperseg=625, nfft=625)
#
# print(f)
# print(Pxx)


import h5py
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from loguru import logger
import time

# 로그 설정 (필요시 파일에 저장)
logger.add("execution_times.log", format="{time} {level} {message}", level="INFO")

# 파일 경로 설정
file_name = r"C:\Users\MSI\project\DAS\krri\0000006155_2024-07-15_06.34.33.25722.hdf5"

# 파일 읽기 시간 측정
start_time = time.time()
with h5py.File(file_name, 'r') as h5file:
    fs = 2500
    diff_phase = h5file['DAS'][:2500, 200]
file_read_time = time.time()
logger.info(f"File read time: {file_read_time - start_time:.4f} seconds")

# 데이터 변환 및 누적합 계산 시간 측정
phase_s64_T = np.int64(diff_phase)
data_phase = np.cumsum(phase_s64_T, axis=0) * (np.pi / 2**15)
cumsum_time = time.time()
logger.info(f"Cumsum calculation time: {cumsum_time - file_read_time:.4f} seconds")

# PSD 계산 시간 측정
f, S = scipy.signal.periodogram(data_phase, fs=fs, scaling='density')
psd_time = time.time()
logger.info(f"PSD calculation time: {psd_time - cumsum_time:.4f} seconds")

plt.semilogy(f,S)
plt.ylim([1e-7, 1e2])
plt.xlim([150, 250])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

f, Pxx = scipy.signal.welch(data_phase, fs=fs, nperseg=625, nfft=625)


plt.semilogy(f, Pxx)
plt.xlim([150, 250])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()
