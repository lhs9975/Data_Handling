import os
from PIL import Image

# 디렉토리 경로 설정
directory = r'C:\Users\MSI\Desktop\company\develop\DAS\Leak_Classification\detect_image'

# 디렉토리 내의 모든 파일을 확인
for filename in os.listdir(directory):
    # 이미지 파일인지 확인 (jpg, png 등)
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # 파일 경로 생성
        img_path = os.path.join(directory, filename)
        # 이미지 로드
        img = Image.open(img_path)
        # 이미지 모드에 따라 채널 수 계산
        mode_to_channels = {
            "1": 1,   # 1-bit pixels, black and white, stored with one pixel per byte
            "L": 1,   # 8-bit pixels, grayscale
            "P": 1,   # 8-bit pixels, mapped to any other mode using a color palette
            "RGB": 3, # 3x8-bit pixels, true color
            "RGBA": 4,# 4x8-bit pixels, true color with transparency mask
            "CMYK": 4,# 4x8-bit pixels, color separation
            "YCbCr": 3,# 3x8-bit pixels, color video format
            "LAB": 3, # 3x8-bit pixels, L*a*b color space
            "HSV": 3, # 3x8-bit pixels, Hue, Saturation, Value color space
            "I": 1,   # 32-bit signed integer pixels
            "F": 1    # 32-bit floating point pixels
        }
        channels = mode_to_channels.get(img.mode, "Unknown mode")
        print(f"{filename}: {img.mode} mode with {channels} channel(s)")
