#!/usr/bin/env python3
#날짜기준 평균값 계산
import pandas as pd

#파일 불러오기
data_frame = pd.read_csv('output01.csv', index_col = None, encoding='cp949')

#해역별로 구분하는 데이터 프레임
Sea_area_df = data_frame[data_frame.loc[:,'Sea_area']=='동중국해']

#새로운 데이터프레임
df = pd.DataFrame(columns=['Sea_area','Date','Temperature_avg', 'Salinity_avg', 'Dissolved Oxygen_avg', \
    'Phosphate Phosphorus_avg', 'Nitrous Acid Nitrogen_avg', 'Nitric Acid Nitrogen_avg', 'Silicic Acid Silicon_avg'])
 
#해역
e_Temp = Sea_area_df['Temperature'].groupby(Sea_area_df['Observation Date'])
i = 0
for j in range(len(e_Temp)+3):
    df.loc[i, 'Sea_area'] = '동중국해'
    i += 1

#날짜 (1~12월) 입력
for i in range(1, 13):
    df.loc[i-1, 'Date'] = i

#수온평균, 데이터가 없는 달에는 Null값 입력
j = 0
for i in range(len(e_Temp)+2):
    if df.loc[i, 'Date'] == e_Temp.mean().index[j]:
        df.loc[i, 'Temperature_avg'] = round(e_Temp.mean().values[j], 3)
        j += 1
    else:
        df.loc[i, 'Temperature_avg'] = None

#염분 평균
e_Salinity = Sea_area_df['Salinity'].groupby(Sea_area_df['Observation Date'])
j = 0
for i in range(len(e_Temp)+2):
    if df.loc[i, 'Date'] == e_Salinity.mean().index[j]:
        df.loc[i, 'Salinity_avg'] = round(e_Salinity.mean().values[j], 3)
        j += 1
    else:
        df.loc[i, 'Salinity_avg'] = None

#용존산소 평균
e_Oxygen = Sea_area_df['Dissolved Oxygen'].groupby(Sea_area_df['Observation Date'])
j = 0
for i in range(len(e_Temp)+2):
    if df.loc[i, 'Date'] == e_Oxygen.mean().index[j]:
        df.loc[i, 'Dissolved Oxygen_avg'] = round(e_Oxygen.mean().values[j], 3)
        j += 1
    else:
        df.loc[i, 'Dissolved Oxygen_avg'] = None

#인산염인 평균
e_Phosphate = Sea_area_df['Phosphate Phosphorus'].groupby(Sea_area_df['Observation Date'])
j = 0
for i in range(len(e_Temp)+2):
    if df.loc[i, 'Date'] == e_Phosphate.mean().index[j]:
        df.loc[i, 'Phosphate Phosphorus_avg'] = round(e_Phosphate.mean().values[j], 3)
        j += 1
    else:
        df.loc[i, 'Phosphate Phosphorus_avg'] = None

#아질산질소 평균
e_Nitrous = Sea_area_df['Nitrous Acid Nitrogen'].groupby(Sea_area_df['Observation Date'])
j = 0
for i in range(len(e_Temp)+2):
    if df.loc[i, 'Date'] == e_Nitrous.mean().index[j]:
        df.loc[i, 'Nitrous Acid Nitrogen_avg'] = round(e_Nitrous.mean().values[j], 3)
        j += 1
    else:
        df.loc[i, 'Nitrous Acid Nitrogen_avg'] = None

#질산규소 평균
e_Nitric = Sea_area_df['Nitric Acid Nitrogen'].groupby(Sea_area_df['Observation Date'])
j = 0
for i in range(len(e_Temp)+2):
    if df.loc[i, 'Date'] == e_Nitric.mean().index[j]:
        df.loc[i, 'Nitric Acid Nitrogen_avg'] = round(e_Nitric.mean().values[j], 3)
        j += 1
    else:
        df.loc[i, 'Nitric Acid Nitrogen_avg'] = None

#규산수소 평균
e_Silicic = Sea_area_df['Silicic Acid Silicon'].groupby(Sea_area_df['Observation Date'])  
j = 0
for i in range(len(e_Temp)+2):
    if df.loc[i, 'Date'] == e_Silicic.mean().index[j]:
        df.loc[i, 'Silicic Acid Silicon_avg'] = round(e_Silicic.mean().values[j], 3)
        j += 1
    else:
        df.loc[i, 'Silicic Acid Silicon_avg'] = None

#출력
df.to_csv('output02-4.csv', index= None, encoding='cp949')
