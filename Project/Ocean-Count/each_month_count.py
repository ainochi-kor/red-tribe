#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

input_file = 'output04_remake.csv'
data_frame = pd.read_csv(input_file, index_col = None, encoding='cp949')

month_data = []
cnt = 0
data_frame_value_meets_condition = []
months = []
for month in range(1,13):
    months.append(month)
    for i in range(len(data_frame)) :
        if data_frame.iloc[i,0] == month :
            cnt = cnt + 1
            print(cnt)
    month_data.append(cnt)
    cnt = 0

print(month_data)


#막대그래프 만들기
plt.style.use('ggplot')
month_index = range(len(months))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(month_index, month_data, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(month_index, months, rotation=0, fontsize='small')
plt.xlabel('month')
plt.ylabel('red tride amount')
plt.title(' month red tride all amount of 2000~2017 years')
#plt.savefig('red_tride_month_plot.png', dpi=400, bbox_inches='tight')
plt.show()
