#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

input_file = 'output04_remake_year.csv'
data_frame = pd.read_csv(input_file, index_col = None, encoding='cp949')

year_data = []
cnt = 0
cnts = 0
data_frame_value_meets_condition = []
years = []
for year in range(2000,2018):
    years.append(cnts)
    for i in range(len(data_frame)) :
        if data_frame.iloc[i,0] == year :
            cnt = cnt + 1
    cnts = cnts + 1
    print(cnt)
    year_data.append(cnt)
    cnt = 0
    
print(year_data)

#막대그래프 만들기
plt.style.use('ggplot')
year_index = range(len(years))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(year_index, year_data, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(year_index, years, rotation=0, fontsize='small')
plt.xlabel('years')
plt.ylabel('red tride amount')
plt.title(' red tride all amount of 2000~2017 years')
#plt.savefig('red_tride_month_plot.png', dpi=400, bbox_inches='tight')
plt.show()
