# import h5py
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal.windows import blackmanharris
#
# # Load Phase HDF5 file
# file_name = r"I:\200421 digging\0000065232_2020-04-21_01.39.43.47368.hdf5"
#
# with h5py.File(file_name, 'r') as h5file:
#     fs = 2000
#     dataset = h5file['DAS']
#     total_length = dataset.shape[0]
#     chunk_size = 30000
#
#     for start in range(0, total_length, chunk_size):
#         end = start + chunk_size
#         diff_phase = h5file['DAS'][start:end, :]
#         phase_s64_T = np.int64(diff_phase)  # Create a 64-bit int copy for accumulation
#
#         # Accumulate differential phase to obtain phase
#         phase_s64_T = np.cumsum(phase_s64_T, axis=0)
#         phase = phase_s64_T * np.pi / 2 ** 15  # Create a double copy and convert to radians
#
#         fft_size = int(fs * 0.25)
#
#         group_of_low_freq_bounds = [0, 8, 20, 48, 100]
#         group_of_high_freq_bounds = [8, 20, 48, 100, fs / 2]
#         count_of_bands = 5
#
#         group_of_low_freq_indices = np.ceil(np.array(group_of_low_freq_bounds) / (fs / fft_size)).astype(int)
#         group_of_high_freq_indices = np.ceil(np.array(group_of_high_freq_bounds) / (fs / fft_size)).astype(int)
#
#         fft_window = blackmanharris(fft_size)
#         fft_window_array = np.tile(fft_window, (phase.shape[1], 1)).T
#         window_power_adjustment = np.sum(fft_window ** 2)
#
#         count_of_blocks = phase.shape[0] // fft_size
#         fbe_store = np.zeros((count_of_bands, phase.shape[1], count_of_blocks), dtype=np.float32)
#
#         for k in range(count_of_blocks):
#             data = phase[k * fft_size:(k + 1) * fft_size, :]
#
#             # The de-mean operation and cast to float32
#             mn = np.mean(data, axis=0)
#             data = data - mn
#             data = data.astype(np.float32)
#
#             windowed_phase = data * fft_window_array
#             fft_data_c = np.fft.fft(windowed_phase, n=fft_size, axis=0)
#
#             if fft_size % 2 == 1:  # Odd
#                 select = np.arange((fft_size + 1) // 2)
#                 fft_data_r = np.abs(fft_data_c[select, :]) ** 2
#                 fft_data_r[1:] = fft_data_r[1:] * 2
#             else:  # Even
#                 select = np.arange(fft_size // 2 + 1)
#                 fft_data_r = np.abs(fft_data_c[select, :]) ** 2
#                 fft_data_r[1:-1] = fft_data_r[1:-1] * 2
#
#             fft_data_r = fft_data_r / (window_power_adjustment * fs)
#
#             for i in range(count_of_bands):
#                 fbe_store[i, :, k] = np.mean(fft_data_r[group_of_low_freq_indices[i]:group_of_high_freq_indices[i], :],
#                                              axis=0)
#             fbe_store[:, :, k] = 10 * np.log10(fbe_store[:, :, k])
#
#             group_of_fbe = [fbe_store[x, :, :].T for x in range(count_of_bands)]
#
#             print(group_of_fbe[3].shape)
#
#         # 예제 데이터 (주어진 데이터로 교체하세요)
#         data = group_of_fbe[3]
#
#         # X와 Y 좌표 생성
#         x = np.arange(data.shape[1])
#         y = np.arange(data.shape[0])
#         X, Y = np.meshgrid(x, y)
#
#         # 플롯 생성
#         plt.figure(figsize=(12, 8))
#
#         # 워터폴 플롯 (pcolormesh)
#         plt.pcolormesh(X, Y, data, shading='auto', cmap='viridis', vmin=-70, vmax=0)
#         plt.colorbar(label='Amplitude')
#
#         plt.xlabel('X')
#         plt.ylabel('Y')
#         plt.title('Waterfall Plot with Amplitude as Color')
#
#         plt.show()

import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import blackmanharris
import glob
import os

# # Input directory containing HDF5 files
# input_dir = r"C:\Users\MSI\Desktop\company\develop"
# output_dir = r"C:\Users\MSI\Desktop\company\develop\APSensing"
#
# # Ensure output directory exists
# os.makedirs(output_dir, exist_ok=True)
#
# # Find all HDF5 files in the input directory
# hdf5_files = glob.glob(os.path.join(input_dir, "*.hdf5"))
#
# for file_name in hdf5_files:
#     with h5py.File(file_name, 'r') as h5file:
#         fs = 2500
#         dataset = h5file['DAS']
#         total_length = dataset.shape[0]
#         chunk_size = 37000
#
#         for start in range(0, total_length, chunk_size):
#             end = start + chunk_size
#             diff_phase = h5file['DAS'][start:end, 26100:26300]
#             phase_s64_T = np.int64(diff_phase)  # Create a 64-bit int copy for accumulation
#
#             # Accumulate differential phase to obtain phase
#             phase_s64_T = np.cumsum(phase_s64_T, axis=0)
#             phase = phase_s64_T * np.pi / 2 ** 15  # Create a double copy and convert to radians
#
#             fft_size = int(fs * 0.25)
#
#             group_of_low_freq_bounds = [0, 8, 20, 48, 100]
#             group_of_high_freq_bounds = [8, 20, 48, 100, fs / 2]
#             count_of_bands = 5
#
#             group_of_low_freq_indices = np.ceil(np.array(group_of_low_freq_bounds) / (fs / fft_size)).astype(int)
#             group_of_high_freq_indices = np.ceil(np.array(group_of_high_freq_bounds) / (fs / fft_size)).astype(int)
#
#             fft_window = blackmanharris(fft_size)
#             fft_window_array = np.tile(fft_window, (phase.shape[1], 1)).T
#             window_power_adjustment = np.sum(fft_window ** 2)
#
#             count_of_blocks = phase.shape[0] // fft_size
#             fbe_store = np.zeros((count_of_bands, phase.shape[1], count_of_blocks), dtype=np.float32)
#
#             for k in range(count_of_blocks):
#                 data = phase[k * fft_size:(k + 1) * fft_size, :]
#
#                 # The de-mean operation and cast to float32
#                 mn = np.mean(data, axis=0)
#                 data = data - mn
#                 data = data.astype(np.float32)
#
#                 windowed_phase = data * fft_window_array
#                 fft_data_c = np.fft.fft(windowed_phase, n=fft_size, axis=0)
#
#                 if fft_size % 2 == 1:  # Odd
#                     select = np.arange((fft_size + 1) // 2)
#                     fft_data_r = np.abs(fft_data_c[select, :]) ** 2
#                     fft_data_r[1:] = fft_data_r[1:] * 2
#                 else:  # Even
#                     select = np.arange(fft_size // 2 + 1)
#                     fft_data_r = np.abs(fft_data_c[select, :]) ** 2
#                     fft_data_r[1:-1] = fft_data_r[1:-1] * 2
#
#                 fft_data_r = fft_data_r / (window_power_adjustment * fs)
#
#                 for i in range(count_of_bands):
#                     fbe_store[i, :, k] = np.mean(
#                         fft_data_r[group_of_low_freq_indices[i]:group_of_high_freq_indices[i], :], axis=0)
#                 fbe_store[:, :, k] = 10 * np.log10(fbe_store[:, :, k])
#
#             group_of_fbe = [fbe_store[x, :, :].T for x in range(count_of_bands)]
#
#             # Plot and save the waterfall plot for one of the frequency bands
#             data = group_of_fbe[3]
#
#             # X와 Y 좌표 생성
#             x = np.arange(data.shape[1])
#             y = np.arange(data.shape[0])
#             X, Y = np.meshgrid(x, y)
#
#             # 플롯 생성
#             plt.figure(figsize=(16, 9))
#
#             # 워터폴 플롯 (pcolormesh)
#             plt.pcolormesh(X, Y, data, shading='auto', cmap='viridis', vmin=-70, vmax=0)
#             plt.colorbar(label='Amplitude')
#
#             plt.xlabel('X')
#             plt.ylabel('Y')
#             plt.title(f'Waterfall Plot with Amplitude as Color - Band 3 - Samples {start} to {end}')
#
#             output_file = os.path.join(output_dir,
#                                        f'waterfall_band_3_{start}_{end}_{os.path.basename(file_name)}.jpg')
#             plt.savefig(output_file, format='jpg', bbox_inches='tight', pad_inches=0)
#             plt.close()  # Close the plot to free up memory


# ----------------------------------------------------------------------------------------------------------------------

import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import blackmanharris
import os

# 디렉토리 경로 설정
directory_path = r"H:\240821_osong_hdf5\240507"
fs = 2500
chunk_size = 150000
fft_size = int(fs * 0.25)
group_of_low_freq_bounds = [0, 8, 20, 48, 100]
group_of_high_freq_bounds = [8, 20, 48, 100, fs / 2]
count_of_bands = 5

group_of_low_freq_indices = np.ceil(np.array(group_of_low_freq_bounds) / (fs / fft_size)).astype(int)
group_of_high_freq_indices = np.ceil(np.array(group_of_high_freq_bounds) / (fs / fft_size)).astype(int)

fft_window = blackmanharris(fft_size)
window_power_adjustment = np.sum(fft_window ** 2)

# 디렉토리 내의 모든 HDF5 파일에 대해 처리
for file_name in os.listdir(directory_path):
    if file_name.endswith(".hdf5"):
        file_path = os.path.join(directory_path, file_name)

        with h5py.File(file_path, 'r') as h5file:
            dataset = h5file['DAS']
            total_length = dataset.shape[0]

            for start in range(0, total_length, chunk_size):
                end = start + chunk_size
                diff_phase = h5file['DAS'][start:end, :3000]
                phase_s64_T = np.int64(diff_phase)  # Create a 64-bit int copy for accumulation

                # Accumulate differential phase to obtain phase
                phase_s64_T = np.cumsum(phase_s64_T, axis=0)
                phase = phase_s64_T * np.pi / 2 ** 15  # Convert to radians

                fft_window_array = np.tile(fft_window, (phase.shape[1], 1)).T
                count_of_blocks = phase.shape[0] // fft_size
                fbe_store = np.zeros((count_of_bands, phase.shape[1], count_of_blocks), dtype=np.float32)

                for k in range(count_of_blocks):
                    data = phase[k * fft_size:(k + 1) * fft_size, :]

                    # De-mean operation and cast to float32
                    mn = np.mean(data, axis=0)
                    data = data - mn
                    data = data.astype(np.float32)

                    windowed_phase = data * fft_window_array
                    fft_data_c = np.fft.fft(windowed_phase, n=fft_size, axis=0)

                    # Select the appropriate frequency range
                    if fft_size % 2 == 1:  # Odd
                        select = np.arange((fft_size + 1) // 2)
                        fft_data_r = np.abs(fft_data_c[select, :]) ** 2
                        fft_data_r[1:] = fft_data_r[1:] * 2
                    else:  # Even
                        select = np.arange(fft_size // 2 + 1)
                        fft_data_r = np.abs(fft_data_c[select, :]) ** 2
                        fft_data_r[1:-1] = fft_data_r[1:-1] * 2

                    fft_data_r = fft_data_r / (window_power_adjustment * fs)

                    for i in range(count_of_bands):
                        fbe_store[i, :, k] = np.mean(
                            fft_data_r[group_of_low_freq_indices[i]:group_of_high_freq_indices[i], :], axis=0
                        )
                    fbe_store[:, :, k] = 10 * np.log10(fbe_store[:, :, k])

                # Example data for plotting
                data = fbe_store[3, :, :].T

                # Create X and Y coordinates
                x = np.arange(data.shape[1])
                y = np.arange(data.shape[0])
                X, Y = np.meshgrid(x, y)

                # Plot the data
                plt.figure(figsize=(12, 8))
                plt.pcolormesh(X, Y, data, shading='auto', cmap='viridis', vmin=-40, vmax=-10)
                plt.colorbar(label='Amplitude')

                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title(f'Waterfall Plot for {file_name} - Chunk {start // chunk_size + 1}')

                plt.show()
