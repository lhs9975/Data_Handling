import os
from PIL import Image

# 변환할 디렉토리 경로
directory = r'C:\Users\MSI\Desktop\company\develop\DAS\Leak_Classification\dataset\hammer'

# 디렉토리 내의 모든 파일을 확인
for filename in os.listdir(directory):
    # .png 확장자 파일만 선택
    if filename.endswith(".png"):
        # 파일 경로를 생성
        png_path = os.path.join(directory, filename)
        # 이미지 로드
        img = Image.open(png_path)
        # .png 확장자를 .jpg로 변경한 파일 이름 생성
        jpg_filename = filename.replace(".png", ".jpg")
        jpg_path = os.path.join(directory, jpg_filename)
        # 이미지 RGB로 변환 및 저장 (RGBA가 아닌 경우에만 변환)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(jpg_path, "JPEG")
        print(f"Converted {png_path} to {jpg_path}")
