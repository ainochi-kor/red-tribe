#!/usr/bin/env python3
# 필요한 열 필터링
import pandas as pd

#경로
input_file = 'ocean_all_data.csv'
output_file = 'output01.csv'

#파일 불러오기
data_frame = pd.read_csv(input_file,index_col= None, encoding='cp949')

#loc는 열 이름을 말하는데. 숨겨진 이스케이프 문자가 많아서 iloc로 해당 열 번호 입력
data_frame = data_frame.iloc[:,[6,8,10,12,15,16,17,18]]  

#파일 만들기
data_frame.to_csv(output_file, index = None, encoding = 'cp949')
