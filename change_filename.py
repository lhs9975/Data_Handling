import os

def rename_files(directory, prefix):
    i = 0
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            os.rename(os.path.join(directory, filename), os.path.join(directory, f"{prefix}_{i}.jpg"))
            i += 1

# 함수를 호출하여 파일 이름을 변경합니다.
# 'directory'는 파일이 있는 디렉토리의 경로이며, 'prefix'는 새 파일 이름의 접두사입니다.
rename_files(r'C:\Users\MSI\Desktop\test\test2\water', 'train_water')
