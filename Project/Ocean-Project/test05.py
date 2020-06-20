#!/usr/bin/env python3 
# 날짜별 평균값을 구하여 따로 csv에 저장, 헤더행 추가
import pandas as pd

#파일 변수로 일단 불러오기. 사실상 문자열로 인지 하긴 할거임. 
input_file = 'output03.csv'

#헤더리스트를 미리 리스트로 구비해놓음.
header_list = ['Observation Date', 'Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon', 'On/Off', 'Grouped_Date', 'Avg_Temp', 'Avg_Sal', 'Avg_Oxy', 'Avg_Phosphorus', 'Avg_Nitrous', 'Avg_Nitric', 'Avg_Silicon']

#팬더스의 데이터 프레임 형식으로 csv 파일을 읽어옴. 네임을 추가하는건데 header_list로
#추가했다. 왜 네임에 추가했는지 모루겠다. 헤더에서도 된다.(리스트형으로 )
data_frame = pd.read_csv(input_file, header=None, names=header_list)

#위에 만들어 놓았던,데이터 프레임에서 온도 부분의 열에서 data_frampe
#groupby가 많이 쓰이는데, 여러가지를 사용할 수 있다.
#파일을 전체적으로 찝어서 뭔가를 하기 위해서 사용하는데 그 찝는 기능을 한다.
#나누거나 합치거나 찾거나 등등 다 가능하다.

#데이터 프레임에서 온도 부분을 첫번쨰 날짜와 찝어준거죠.?
#데이터프레임에 딕셔너리 같은 느낌으로 자료 그룹의 2개를 놓고 행할때 쓰기 위해서 
#이런식으로 구분.
grouped_temperature = data_frame['Temperature'].groupby(data_frame['Observation Date'])
#data_frame['Avg_Temp'][0] = str(grouped_temperature.mean())

i = 0
#그룹화 시킨 데이터 프레임의 온도 열과 날짜열을 전체적으로 평균을 구하고,
for index in grouped_temperature.mean().index: #딕셔너리랑 비슷한 시리즈 type index,value로 나눠져있음
    data_frame['Grouped_Date'][i] = index
    i += 1
    
j = 0
for value in grouped_temperature.mean().values:
    data_frame['Avg_Temp'][j] = value
    j += 1

grouped_salinity = data_frame['Salinity'].groupby(data_frame['Observation Date'])
#data_frame['Avg_Sal'][0] = str(grouped_salinity.mean())
i = 0
for value in grouped_salinity.mean().values:
    data_frame['Avg_Sal'][i] = value
    i += 1

grouped_Oxygen = data_frame['Dissolved Oxygen'].groupby(data_frame['Observation Date'])
#data_frame['Avg_Oxy'][0] = str(grouped_Oxygen.mean())
i = 0
for value in grouped_Oxygen.mean().values:
    data_frame['Avg_Oxy'][i] = value
    i += 1

#인산염인, 아질산질소, 질산규소의 type이 object로 있어서 형변환 (errors='coerce' : 오류데이터인 경우 Nan으로 변환)
data_frame['Phosphate Phosphorus'] = pd.to_numeric(data_frame['Phosphate Phosphorus'], errors='coerce')
data_frame['Nitrous Acid Nitrogen'] = pd.to_numeric(data_frame['Nitrous Acid Nitrogen'], errors='coerce')
data_frame['Nitric Acid Nitrogen'] = pd.to_numeric(data_frame['Nitric Acid Nitrogen'], errors='coerce')

grouped_Phosphorus = data_frame['Phosphate Phosphorus'].groupby(data_frame['Observation Date'])
#data_frame['Avg_Oxy'][0] = str(grouped_Oxygen.mean())
i = 0
for value in grouped_Phosphorus.mean().values: 
    data_frame['Avg_Phosphorus'][i] = value
    i += 1

grouped_Nitrous = data_frame['Nitrous Acid Nitrogen'].groupby(data_frame['Observation Date'])
#data_frame['Avg_Oxy'][0] = str(grouped_Oxygen.mean())
i = 0
for value in grouped_Nitrous.mean().values:
    data_frame['Avg_Nitrous'][i] = value
    i += 1
    
grouped_Nitric = data_frame['Nitric Acid Nitrogen'].groupby(data_frame['Observation Date'])
#data_frame['Avg_Oxy'][0] = str(grouped_Oxygen.mean())
i = 0
for value in grouped_Nitric.mean().values:
    data_frame['Avg_Nitric'][i] = value
    i += 1
    
grouped_Silicon = data_frame['Silicic Acid Silicon'].groupby(data_frame['Observation Date'])
#data_frame['Avg_Oxy'][0] = str(grouped_Oxygen.mean())
i = 0
for value in grouped_Silicon.mean().values:
    data_frame['Avg_Silicon'][i] = value
    i += 1  

#해양관측정보와 평균값들을 다른 파일로 처리
data_frames = data_frame.loc[:, ['Grouped_Date','Avg_Temp','Avg_Sal','Avg_Oxy', 'Avg_Phosphorus', 'Avg_Nitrous', 'Avg_Nitric', 'Avg_Silicon']]
data_frame = data_frame.loc[:, ['Observation Date', 'Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon', 'On/Off']]

data_frames.to_csv('result02.csv', index=False)
data_frame.to_csv('output04.csv', index=False)
