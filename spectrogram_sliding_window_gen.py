# import h5py
# import matplotlib.pyplot as plt
# import scipy.signal as signal
# import numpy as np
# from scipy.signal.windows import blackmanharris
# import os
#
# event_name = "filling_the_hole"
# phase_file_name = 23655
# position = 1218
#
# # 파일 이름 설정
# file_name = r"H:\APSensing_TPI\20230308-tpi\08-03-2023\Phase Data\0000023655_2023-03-08_10.03.41.95429.hdf5"
#
# # 저장 폴더 설정
# output_folder = rf"C:\Users\MSI\Desktop\company\develop\DAS\Leak_Classification\dataset\APS_TPI_SLIDING_WINDOW\{event_name}"
# # output_folder = rf"C:\Users\MSI\Desktop\company\develop\DAS\Leak_Classification\dataset\APS_TPI_SLIDING_WINDOW\test"
# os.makedirs(output_folder, exist_ok=True)
#
# with h5py.File(file_name, 'r', libver='latest') as f:
#     fs = 1000
#     diff_phase = f['DAS'][:, position]
#     print(f['DAS'].shape)
#     print(diff_phase.shape)
#     phase_s64_T = np.int64(diff_phase)
#
# data_phase = np.cumsum(phase_s64_T, axis=0) * (np.pi / 2 ** 15)
#
# # 고역 통과 필터 적용
# cutoff = 4
# nyq = fs / 2
# b, a = signal.butter(5, cutoff / nyq, btype='high', analog=False)
# data_phase_filtered = signal.filtfilt(b, a, data_phase)
#
# # 슬라이딩 윈도우 설정
# window_size = 15000
# step = 250
# end_index = data_phase_filtered.shape[0] - window_size
#
# for start in range(0, end_index, step):
#     segment = data_phase_filtered[start:start + window_size]
#
#     # STFT 계산
#     f, t, zxx = signal.stft(segment, fs=fs, window='blackmanharris', nfft=250, nperseg=250, boundary='zeros')
#
#     # 스펙트로그램 이미지 생성
#     plt.figure()
#     plt.pcolormesh(t, f, np.abs(zxx), cmap='plasma', vmax=0.03)
#     plt.ylim(0, 200)
#     plt.axis('off')
#
#     # 이미지 저장
#     file_path = os.path.join(output_folder, f"{event_name}_{phase_file_name}_{position}_{start}.png")
#     plt.savefig(file_path, format='png', bbox_inches='tight', pad_inches=0)
#     plt.close()
#
#     print(f"Saved {file_path}")


import h5py
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
from scipy.signal.windows import blackmanharris
import os

event_name = "pile_driving_digging"
phase_file_name = 23677

# 파일 이름 설정
file_name = r"H:\APSensing_TPI\20230308-tpi\09-03-2023\Phase Data\0000024171_2023-03-09_08.21.38.77847.hdf5"

# 저장 폴더 설정
output_folder = rf"C:\Users\MSI\Desktop\company\develop\DAS\Leak_Classification\dataset\APS_TPI_SLIDING_WINDOW\0.03"
os.makedirs(output_folder, exist_ok=True)

# position 범위 설정
position_start = 3974
position_end = 3978

# 각 position에 대해 반복
for position in range(position_start, position_end + 1):
    with h5py.File(file_name, 'r', libver='latest') as f:
        fs = 1000
        diff_phase = f['DAS'][:, position]
        print(f'Processing position {position}: {f["DAS"].shape}')
        phase_s64_T = np.int64(diff_phase)

    data_phase = np.cumsum(phase_s64_T, axis=0) * (np.pi / 2 ** 15)

    # 고역 통과 필터 적용
    cutoff = 4
    nyq = fs / 2
    b, a = signal.butter(5, cutoff / nyq, btype='high', analog=False)
    data_phase_filtered = signal.filtfilt(b, a, data_phase)

    # 슬라이딩 윈도우 설정
    window_size = 15000
    step = 250
    end_index = data_phase_filtered.shape[0] - window_size

    for start in range(0, end_index, step):
        segment = data_phase_filtered[start:start + window_size]

        # STFT 계산
        f, t, zxx = signal.stft(segment, fs=fs, window='blackmanharris', nfft=250, nperseg=250, boundary='zeros')

        # 스펙트로그램 이미지 생성
        plt.figure()
        plt.pcolormesh(t, f, np.abs(zxx), cmap='plasma', vmax=0.03)
        plt.ylim(0, 500)
        plt.axis('off')

        # 이미지 저장
        file_path = os.path.join(output_folder, f"{event_name}_{phase_file_name}_{position}_{start}.png")
        plt.savefig(file_path, format='png', bbox_inches='tight', pad_inches=0)
        plt.close()

        print(f"Saved {file_path}")
