# import os
# import shutil
#
# source_folder = r'E:\MLTA_TEST_05_13'  # 소스 폴더 경로를 지정하세요.
# target_folder_base = r'C:\Users\MSI\Desktop\회사\개발\MLTA\dataset\company_data\tra_data\time_60_split'  # 타겟 폴더 베이스 경로를 지정하세요.
# files_per_batch = 300  # 한 폴더 당 파일 개수
#
# # 소스 폴더에서 .tra 파일 목록을 가져옵니다.
# file_list = [f for f in os.listdir(source_folder) if f.endswith('.tra')]
#
# # 파일들을 500개씩 나누어 저장합니다.
# for i in range(0, len(file_list), files_per_batch):
#     # 타겟 폴더를 생성합니다. 폴더 이름 예시: 'batch_1', 'batch_2', ...
#     batch_folder = os.path.join(target_folder_base, 'batch_' + str(i // files_per_batch + 1))
#     os.makedirs(batch_folder, exist_ok=True)
#
#     # 파일을 타겟 폴더로 이동합니다.
#     for file in file_list[i:i + files_per_batch]:
#         shutil.copy(os.path.join(source_folder, file), os.path.join(batch_folder, file))
#
# # 모든 파일을 처리한 후 스크립트가 완료됩니다.
# print("Files have been moved to respective folders.")

import os
import shutil

source_folder = r'C:\Users\MSI\Desktop\회사\개발\MLTA\dataset\real_data\GS_ENR\tra\ch2\all'  # 소스 폴더 경로를 지정하세요.
target_folder_base = r'C:\Users\MSI\Desktop\회사\개발\MLTA\dataset\real_data\GS_ENR\tra\ch2'  # 타겟 폴더 베이스 경로를 지정하세요.
files_per_batch = 200  # 한 폴더 당 파일 개수

# 소스 폴더에서 .tra 파일 목록을 가져옵니다.
file_list = [f for f in os.listdir(source_folder) if f.endswith('.tra')]

# 파일 목록을 이름 순서대로 정렬합니다.
file_list.sort()

# 파일들을 300개씩 나누어 저장합니다.
for i in range(0, len(file_list), files_per_batch):
    # 타겟 폴더를 생성합니다. 폴더 이름 예시: 'batch_1', 'batch_2', ...
    batch_folder = os.path.join(target_folder_base, 'batch_' + str(i // files_per_batch + 1))
    os.makedirs(batch_folder, exist_ok=True)

    # 파일을 타겟 폴더로 복사합니다.
    for file in file_list[i:i + files_per_batch]:
        shutil.copy(os.path.join(source_folder, file), os.path.join(batch_folder, file))

# 모든 파일을 처리한 후 스크립트가 완료됩니다.
print("Files have been moved to respective folders.")
