import os
import json

# 변환할 JSON 파일들이 있는 디렉토리 경로 설정
input_directory = r"E:\작물 병 데이터\104.식물 병 유발 통합 데이터\01.데이터\2.Validation\라벨링데이터\VL1_고추\abnormal_all"
output_directory = r"E:\작물 병 데이터\104.식물 병 유발 통합 데이터\01.데이터\2.Validation\라벨링데이터\VL1_고추\abnormal"

# 출력 디렉토리가 없으면 생성
os.makedirs(output_directory, exist_ok=True)

# 디렉토리 내 모든 JSON 파일에 대해 변환 작업 수행
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):
        json_file_path = os.path.join(input_directory, filename)

        # JSON 파일 로드
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # 이미지 크기 정보
        image_width = data['description']['width']
        image_height = data['description']['height']

        # 바운딩 박스 정보
        bbox = data['annotations']['bbox'][0]
        x = bbox['x']
        y = bbox['y']
        w = bbox['w']
        h = bbox['h']

        # YOLOv5 형식으로 변환
        x_center = (x + w / 2) / image_width
        y_center = (y + h / 2) / image_height
        width = w / image_width
        height = h / image_height

        # class_id는 예제로 0으로 설정
        class_id = 1

        # 변환된 데이터를 YOLOv5 형식으로 텍스트 파일로 저장
        txt_filename = filename.replace('.json', '.txt')
        output_file_path = os.path.join(output_directory, txt_filename)

        with open(output_file_path, 'w') as f:
            f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

        print(f"YOLOv5 라벨 파일이 '{output_file_path}'에 저장되었습니다.")

print("모든 JSON 파일이 변환되었습니다.")
