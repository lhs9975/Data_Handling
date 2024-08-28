import os
import shutil

# 이미지 파일이 저장된 디렉토리 경로 설정
train_directory = r"E:\작물 병 데이터\dataset\train\images"
val_directory = r"E:\작물 병 데이터\dataset\valid\images"

# JSON 파일들이 원래 있던 디렉토리 경로 설정
json_source_directory = r"E:\작물 병 데이터\abnormal_labels"

# JSON 파일이 이동될 디렉토리 경로 설정
json_train_directory = r"E:\작물 병 데이터\dataset\train\labels"
json_val_directory = r"E:\작물 병 데이터\dataset\valid\labels"

# 출력 디렉토리가 없으면 생성
os.makedirs(json_train_directory, exist_ok=True)
os.makedirs(json_val_directory, exist_ok=True)

# 학습용 디렉토리로 이동된 이미지와 동일한 이름의 JSON 파일을 이동
for filename in os.listdir(train_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        json_filename = filename.rsplit('.', 1)[0] + '.txt'
        json_file_path = os.path.join(json_source_directory, json_filename)
        if os.path.exists(json_file_path):
            shutil.move(json_file_path, os.path.join(json_train_directory, json_filename))

# 검증용 디렉토리로 이동된 이미지와 동일한 이름의 JSON 파일을 이동
for filename in os.listdir(val_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        json_filename = filename.rsplit('.', 1)[0] + '.txt'
        json_file_path = os.path.join(json_source_directory, json_filename)
        if os.path.exists(json_file_path):
            shutil.move(json_file_path, os.path.join(json_val_directory, json_filename))

print("JSON 파일이 이미지와 동일한 비율로 학습용과 검증용 디렉토리로 나누어졌습니다.")
