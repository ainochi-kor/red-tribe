#!/usr/bin/env python3
# 발생여부 표시 및 붙이기
import pandas as pd

input_file1 = 'result01.csv'
input_file2 = 'output02.csv'

#헤더와 이름이 없다는 느김으로 파일을 불러서 읽었다..
#csv 파일이 header 줄이 없다고 생각하고 읽고 name 도 없다고 생각하고 읽는 거임..
df1 = pd.read_csv(input_file1, header=None, names=None)
df2 = pd.read_csv(input_file2, header=None, names=None)

#on/off라고 적혀있는 열을 만들어 준 다음에 0으로 값을 다 채움.
df2['ON/OFF'] = 0

#반복에서 df1[0] csv파일이 이상한게 행은 안되고 열만 가능함... 뭐 필요한것만 만든건가.
#아무튼 첫번째 열을 반복하는거임.
for date_index in df1[0]:
    i = 0
    #df1[0]은 리스트형이라서 str, strip을 통해 필요없는 부분을 제거한 후 비교
    #strip은 일단 기본값은 빈 공간 지우는건데.
    #나머지 lstrip이나 rstrip은 왼쪽 오른쪽 지우는 것이다.
    #걍 '을 전부 다 지우고 [왼쪽에 있는거랑 ]오른쪽에 있는거 지움.
    #강제 문자열로 만들어서 그런식으로 처리했습니다.
    date_index = str(date_index).lstrip('[').rstrip(']').strip('\'')
    
    #두번째 파일을 연결해서 첫번째 행을 돌립니다.
    for OD_index in df2[0]:
        #조건을 date_index와 똑같을 경우로 한정시킴. 두 파일 첫번째 부분은 날짜 부분임.
        if date_index == OD_index:
            #데이터 on/off의 헤더가 있는 i 부분의 데이터를 1로 적어놓음.
            df2['ON/OFF'][i] = 1
        #파일을 반복시키기 위해서 공부함.
        i += 1

#마지막 파일을 저장함.
df2.to_csv('output03.csv', index=False, header=None)