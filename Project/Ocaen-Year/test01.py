#!/usr/bin/env python3
#데이터 합치기 및 수심 0으로 필터링

import pandas as pd
import glob
import os

#엑셀파일들 불러오기
excel_files = glob.glob('*xls*')

#csv파일로 변환
for excel in excel_files:

    out = excel.split('.')[0]+'.csv'
    df = pd.read_excel(excel,'정선해양관측정보',index_col = None)
    df.to_csv(out,encoding='cp949',index = False)
    
#현재 디렉토리 파일을 가져옵니다.
input_path = os.getcwd()

#all_files을 불러오는데. glob라는 라이브러리를 기능을 통해서 유닉스 스타일
#경로명을 데리고 와서 os라이브러리의 기능인 경로의 참조를 해서 가져온다.
all_files = glob.glob(os.path.join(input_path,'정선해양관측정보_*.csv*'))

all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None, engine='python', header=1)
    all_data_frames.append(data_frame)
    
#데이터프레임을 합치는 concat메소드 사용.
#axis 0일경우 수직으로 합치고 1일 경우 수평으로 합친다.
all_data_concatenated = pd.concat(all_data_frames, axis=0, ignore_index=True)

#수심 0으로 필터링
all_data_concatenated = all_data_concatenated[all_data_concatenated.iloc[:,7] == 0]

#csv로 만들어서 저장하는데 encoding을 cp949로 안하면 한글 부분이 깨진다.
all_data_concatenated.to_csv('ocean_all_data.csv', index=None, encoding="cp949")
