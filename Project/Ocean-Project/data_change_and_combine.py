#-*- encoding: utf8 -*-

"""
2019-01-23
제작 : 이동현
검수 및 수정 : 김준한

엑셀로 되어 있는 파일을 팬더스 라이브러리를 사용하여서 csv파일로 바꾸고.

팬더스의 csv 파일 처리를 통해서 데이터를 전체다 합한 것이다.
"""

import pandas as pd
import glob
import os

#엑셀파일들을 읽어오기 위해서 .xls 붙은 파일들을 다 참고하여서 읽었다.
excel_files = glob.glob('*xls*')

#그 엑셀파일들 찾은 것들을 하나씩 바꾸기 위해서 반복을 돌렸다.
for excel in excel_files:
    #out 은 csv로 저장될 파일 이름을 저장해주기 위한 프로그램이다.
    #split을 . 기준으로 잘르면 제목 부분과 확장자 부분으로 나누어 지는데.
    #그걸 나눈 리스트의 제목 부분을 없애고 .csv라고 붙혀주어서 파일을 저장한다.
    out = excel.split('.')[0]+'.csv'
    
    #df변수는 팬더스 엑셀 읽어오기로 워크시트를 정선해양관측정보를 읽어온 것이다.
    #index_col = None 하지 않으면 파일에 인덱스 그래도 읽어온다.
    df = pd.read_excel(excel,'정선해양관측정보',index_col = None)
    
    #to_csv라는 팬더스 기능을 이용하여서 만들었다.
    #한글이 있기 때문에 인코딩을 cp949를 이용했다.
    #나중에 이 파일을 읽을때는 ipython으로 돌리기 힘들기 때문에
    #엔진을 python으로 설정해야 줘야한다.
    df.to_csv(out,encoding='cp949',index = False)

#현재 디렉토리 파일을 가져옵니다.
input_path = os.getcwd()

#all_files을 불러오는데. glob라는 라이브러리를 기능을 통해서 유닉스 스타일
#경로명을 데리고 와서 os라이브러리의 기능인 경로의 참조를 해서 가져오는 겁니다.
#자세한 설명은 라이브러리 홈페이지나 제작자에게 물어보자.
all_files = glob.glob(os.path.join(input_path,'정선해양관측정보_*.csv*'))

#데이터를 모두 집어 넣을 dataframe 형식 만들기. 빈 데이터 프레임 제작
all_data_frames = []

#파일 읽어오는 것을 반복하는 것이다.
for file in all_files:
    #데이터 프레임을 읽어오는데 cp949로 인코딩된 한글 파일이기 때문에.
    #ipython을 사용하지 못한다 그러기에 엔진을 python으로 변환해주었다
    #header = 1이라고 한것은 첫 부분 0 부분은 제목이 있어서
    #없애기 위함이다.
    data_frame = pd.read_csv(file, index_col=None, engine='python', header=1)

    #데이터를 빈 데이터프레임에 추가하는 코드이다.
    all_data_frames.append(data_frame)

#데이터프레임을 합치는 concat이라는 메소드가 있어서 사용하는 것이다.
#axis 0일경우 수직으로 합치고 1일 경우 수평으로 합친다.
all_data_concatenated = pd.concat(all_data_frames, axis=0, ignore_index=True)

#수심 0으로 필터링
all_data_concatenated = all_data_concatenated[all_data_concatenated.iloc[:,7] == 0]

#csv로 만들어서 저장하는데 encoding을 cp949로 안하면 한글 부분이 깨진다.
all_data_concatenated.to_csv('ocean_all_data.csv', index=None, encoding="cp949")





