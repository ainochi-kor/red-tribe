#!/usr/bin/env python3
#날짜기준 평균값 계산
import pandas as pd

#파일 불러오기
data_frame = pd.read_csv('output01.csv', index_col = None, encoding='cp949')

#해역별로 구분하는 데이터 프레임
Sea_area_df = data_frame[data_frame.loc[:,'Sea_area']=='남해']

#새로운 데이터프레임
df = pd.DataFrame(columns=['Sea_area','Date','Temperature_avg', 'Salinity_avg', 'Dissolved Oxygen_avg', \
    'Phosphate Phosphorus_avg', 'Nitrous Acid Nitrogen_avg', 'Nitric Acid Nitrogen_avg', 'Silicic Acid Silicon_avg'])
 
#해역
e_Temp = Sea_area_df['Temperature'].groupby(Sea_area_df['Observation Date'])
i = 0
for j in range(2000, 2018):
    df.loc[i, 'Sea_area'] = '남해'
    i += 1

#년도 (2000~2017년) 입력
i=0
for j in range(2000, 2018):
    df.loc[i, 'Date'] = str(j)+str('-08')
    i += 1

#수온평균, 데이터가 없는 달에는 Null값 입력
for i in range(len(e_Temp)):
    df.loc[i, 'Temperature_avg'] = round(e_Temp.mean().values[i], 3)

#염분 평균
e_Salinity = Sea_area_df['Salinity'].groupby(Sea_area_df['Observation Date'])
for i in range(len(e_Temp)):
    df.loc[i, 'Salinity_avg'] = round(e_Salinity.mean().values[i], 3)
        
#용존산소 평균
e_Oxygen = Sea_area_df['Dissolved Oxygen'].groupby(Sea_area_df['Observation Date'])
for i in range(len(e_Temp)):
    df.loc[i, 'Dissolved Oxygen_avg'] = round(e_Oxygen.mean().values[i], 3)

#인산염인 평균
e_Phosphate = Sea_area_df['Phosphate Phosphorus'].groupby(Sea_area_df['Observation Date'])
for i in range(len(e_Temp)):
    df.loc[i, 'Phosphate Phosphorus_avg'] = round(e_Phosphate.mean().values[i], 3)

#아질산질소 평균
e_Nitrous = Sea_area_df['Nitrous Acid Nitrogen'].groupby(Sea_area_df['Observation Date'])
for i in range(len(e_Temp)):
    df.loc[i, 'Nitrous Acid Nitrogen_avg'] = round(e_Nitrous.mean().values[i], 3)

#질산규소 평균
e_Nitric = Sea_area_df['Nitric Acid Nitrogen'].groupby(Sea_area_df['Observation Date'])
for i in range(len(e_Temp)):
    df.loc[i, 'Nitric Acid Nitrogen_avg'] = round(e_Nitric.mean().values[i], 3)

#규산수소 평균
e_Silicic = Sea_area_df['Silicic Acid Silicon'].groupby(Sea_area_df['Observation Date'])  
for i in range(len(e_Temp)):
    df.loc[i, 'Silicic Acid Silicon_avg'] = round(e_Silicic.mean().values[i], 3)

#출력
df.to_csv('output02-2.csv', index= None, encoding='cp949')
