import os
import random
import shutil

# 원본 이미지 디렉토리 경로 설정
source_directory = r"E:\plant_disease_project\dataset\images\abnormal_train\작물보호제처리반응"

# 분할 후 저장할 디렉토리 경로 설정
train_directory = r"E:\plant_disease_project\dataset\images\train"
val_directory = r"E:\plant_disease_project\dataset\images\valid"

# 출력 디렉토리가 없으면 생성
os.makedirs(train_directory, exist_ok=True)
os.makedirs(val_directory, exist_ok=True)

# 이미지 파일 목록 불러오기 (jpg, png 등으로 확장자를 필터링)
image_files = [f for f in os.listdir(source_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

# 이미지 파일을 무작위로 섞기
random.shuffle(image_files)

# 8:2 비율로 나누기
split_index = int(len(image_files) * 0.8)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

# 파일을 각각의 디렉토리로 이동
for file in train_files:
    shutil.move(os.path.join(source_directory, file), os.path.join(train_directory, file))

for file in val_files:
    shutil.move(os.path.join(source_directory, file), os.path.join(val_directory, file))

print(f"이미지 파일이 {len(train_files)}개는 '{train_directory}'로, {len(val_files)}개는 '{val_directory}'로 이동되었습니다.")
