import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 경로
file_path = r"C:\Users\MSI\Desktop\회사\개발\MLTA\dataset\company_data\trace_data_excel\24_05_21_time_10\train_data\combined_temperatures_05_23_original_T.csv"  # 실제 CSV 파일 경로로 변경 필요

# CSV 파일 불러오기
df = pd.read_csv(file_path, index_col=0)

# 컬러맵 생성
plt.figure(figsize=(20, 10))
sns.heatmap(df, cmap='viridis', annot=False)
plt.title('Temperature Data Colormap')
plt.xlabel('Position')
plt.ylabel('Time')
plt.show()
