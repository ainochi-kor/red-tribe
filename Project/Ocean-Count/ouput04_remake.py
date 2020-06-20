#!/usr/bin/env python3

import pandas as pd

#output04.csv를 가져오기.
input_file = 'output04.csv'
from dateutil.parser import parse

#dataframe을 사용하여 구조를 저장.
df1 = pd.read_csv(input_file, index_col = None, encoding='cp949')

#월별 Observation Data를 추출하는 작업.
i = 0
for date_time in df1['Observation Date']:
    df1['Observation Date'][i] = parse(date_time).strftime('%m')
    i = i + 1
 
#염분, 인산염인의 수치가 비정상인 것은 행을 제거함.
df1 = df1[df1['Salinity'].astype(float) < 99.0]
df1 = df1[df1['Silicic Acid Silicon'].astype(float) < 99.0]
df1 = df1.loc[(df1['On/Off']==1),:]

#그 결과 값은 'output04_remake_month.csv로 저장함.
df1.to_csv('output04_remake_month.csv', index = None, encoding = 'cp949')

#년도별 csv파일 추출
df2 = pd.read_csv(input_file, index_col = None, encoding='cp949')
i = 0
for date_time in df2['Observation Date']:
    df2['Observation Date'][i] = parse(date_time).strftime('%Y')
    i = i + 1
 
df2 = df2[df2['Salinity'].astype(float) < 99.0]
df2 = df2[df2['Silicic Acid Silicon'].astype(float) < 99.0]
df2 = df2.loc[(df2['On/Off']==1),:]

df2.to_csv('output04_remake_year.csv', index = None, encoding = 'cp949')
