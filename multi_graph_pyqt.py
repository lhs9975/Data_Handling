# import sys
# import pandas as pd
# import pyqtgraph as pg
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
#
# # D2Coding 폰트 경로 설정
# font_path = 'C:/Windows/Fonts/malgun.ttf'  # D2Coding 폰트 경로 설정
#
# # CSV 파일 로드 (인코딩 지정)
# df = pd.read_csv(r"C:\Users\MSI\Desktop\company\develop\MLTA_Gwangyang\POSCO.csv", encoding='ISO-8859-1', index_col=0)
#
# # 데이터프레임의 컬럼 이름 출력
# print("Columns in DataFrame:", df.columns)
#
# # 열 이름의 공백 제거
# df.columns = df.columns.str.strip()
#
# # 인덱스를 '시간' 컬럼으로 변환
# df.index.name = '시간'
# df.reset_index(inplace=True)
#
# # 시간 컬럼을 datetime 형식으로 변환
# df['시간'] = pd.to_datetime(df['시간'], errors='coerce')
#
# # '2024-07-02 13:40'와 다른 위치의 온도를 6시간 간격으로 추출
# start_time = '2024-07-02 13:40:00'
# end_time = '2024-07-03 13:40:00'
#
# # 플롯할 컬럼 이름 리스트
# columns_to_plot = ['181.75', '197.75', '214.5', '226.5', '239', '251.5', '264.5', '277.5', '290.5', '303.5', '316.5',
#                    '329.5']
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Temperature Data Visualization')
#         self.setGeometry(100, 100, 1000, 800)
#
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         layout = QVBoxLayout()
#         central_widget.setLayout(layout)
#
#         pg.setConfigOptions(antialias=True)  # 더 부드러운 라인
#
#         for column in columns_to_plot:
#             filtered_df = df[(df['시간'] >= start_time) & (df['시간'] < end_time)][['시간', column]]
#             filtered_df.set_index('시간', inplace=True)
#             filtered_df = filtered_df.asfreq('6H').reset_index()
#
#             plot_widget = pg.PlotWidget(title=f'6시간 간격으로 {column} 위치의 온도 변화 (2024년 7월 2일 13:40부터)')
#             layout.addWidget(plot_widget)
#
#             time_in_sec = filtered_df['시간'].astype('int64') // 10 ** 9  # datetime을 초 단위로 변환
#             plot_widget.plot(time_in_sec, filtered_df[column], pen='b', symbol='o')
#             plot_widget.setLabel('left', '온도 (°C)')
#             plot_widget.setLabel('bottom', '시간', units='s', angle=0)
#             plot_widget.getAxis('bottom').setTicks(
#                 [[(v, pd.to_datetime(v * 10 ** 9).strftime('%m-%d %H:%M')) for v in time_in_sec]])
#             plot_widget.showGrid(x=True, y=True)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())

import sys
import pandas as pd
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

# D2Coding 폰트 경로 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # D2Coding 폰트 경로 설정

# CSV 파일 로드 (인코딩 지정)
df = pd.read_csv(r"C:\Users\MSI\Desktop\company\develop\MLTA_Gwangyang\POSCO.csv", encoding='ISO-8859-1', index_col=0)

# 데이터프레임의 컬럼 이름 출력
print("Columns in DataFrame:", df.columns)

# 열 이름의 공백 제거
df.columns = df.columns.str.strip()

# 인덱스를 '시간' 컬럼으로 변환
df.index.name = '시간'
df.reset_index(inplace=True)

# 시간 컬럼을 datetime 형식으로 변환
df['시간'] = pd.to_datetime(df['시간'], errors='coerce')

# '2024-07-02 13:40'와 다른 위치의 온도를 6시간 간격으로 추출
start_time = '2024-07-02 18:00:00'
end_time = '2024-07-11 06:00:00'

# 플롯할 컬럼 이름 리스트
columns_to_plot = ['181.75', '197.75', '214.5', '226.5', '245.25', '261', '277.25', '320.5', '354.5', '399.5', '434.25',
                   '465']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Temperature Data Visualization')
        self.setGeometry(100, 100, 1600, 800)  # 화면을 가로로 길게 설정

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        pg.setConfigOptions(antialias=True)  # 더 부드러운 라인

        for i, column in enumerate(columns_to_plot):
            filtered_df = df[(df['시간'] >= start_time) & (df['시간'] < end_time)][['시간', column]]
            filtered_df.set_index('시간', inplace=True)
            filtered_df = filtered_df.asfreq('12H').reset_index()

            # 글씨 bold체 적용
            plot_widget = pg.PlotWidget(title=f'{column}m')
            plot_widget.setBackground('w')  # 배경을 흰색으로 설정
            time_in_sec = filtered_df['시간'].astype('int64') // 10 ** 9  # datetime을 초 단위로 변환
            plot_widget.plot(time_in_sec, filtered_df[column], pen='b')
            plot_widget.setLabel('left', '온도 (°C)')
            plot_widget.setLabel('bottom', '시간')
            plot_widget.getAxis('bottom').setTicks(
                [[(v, pd.to_datetime(v * 10 ** 9).strftime('%m-%d %H')) for v in time_in_sec]])
            plot_widget.showGrid(x=True, y=True)

            # x축의 최소값과 최대값을 설정하여 모든 점이 표시되도록 함
            plot_widget.setXRange(time_in_sec.min(), time_in_sec.max())

            if i < 6:
                left_layout.addWidget(plot_widget)
            else:
                right_layout.addWidget(plot_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
