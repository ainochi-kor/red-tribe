#!/usr/bin/env python3 
# 로지스틱 회귀분석
import pandas as pd
import statsmodels.api as sm

#header=0은 해더행 무시한다는 의미. 데이터프레임으로 읽음
data_frame = pd.read_csv('output04.csv', header=0)
#종속변수로 선언
dependent_variable = data_frame['On/Off']
#독립변수로 선언
independent_variables = data_frame[['Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']]
#입력변수에 전체 값이 1인 열을 추가
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
#로지스틱 회귀모형에 피팅 (NaN행 무시)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()
#출력
print(logit_model.summary())

#회귀계수 해석
def inverse_logit(model_formula):
    from math import exp
    return (1.0/(1.0+exp(-model_formula)))

#평균값을 입력시 발생확률
at_means = float(logit_model.params[0]) + \
    float(logit_model.params[1])*float(data_frame['Temperature'].mean()) + \
    float(logit_model.params[2])*float(data_frame['Salinity'].mean()) + \
    float(logit_model.params[3])*float(data_frame['Dissolved Oxygen'].mean()) + \
    float(logit_model.params[4])*float(data_frame['Phosphate Phosphorus'].mean()) + \
    float(logit_model.params[5])*float(data_frame['Nitrous Acid Nitrogen'].mean()) + \
    float(logit_model.params[6])*float(data_frame['Nitric Acid Nitrogen'].mean()) + \
    float(logit_model.params[7])*float(data_frame['Silicic Acid Silicon'].mean())

probability = (inverse_logit(at_means))*100
print("7가지 요소들의 평균 값을 입력시 적조발생 확률 : %.3f %%" % probability)

temp_list = []
sal_list = []
oxy_list = []
Phosphate_list = []
Nitrous_list = []
Nitric_list = []
Silicic_list = []

temp_means_list = []
sal_means_list = []
oxy_means_list = []
Phosphate_means_list = []
Nitrous_means_list = []
Nitric_means_list = []
Silicic_means_list = []

for i in range(len(data_frame['Observation Date'])):
    
    temp_means = float(logit_model.params[0]) + \
    float(logit_model.params[1])*float(data_frame['Temperature'][i])
    
    sal_means = float(logit_model.params[0]) + \
    float(logit_model.params[2])*float(data_frame['Salinity'][i])
    
    oxy_means = float(logit_model.params[0]) + \
    float(logit_model.params[3])*float(data_frame['Dissolved Oxygen'][i])
    
    Phosphate_means = float(logit_model.params[0]) + \
    float(logit_model.params[4])*float(data_frame['Phosphate Phosphorus'][i])
    
    Nitrous_means = float(logit_model.params[0]) + \
    float(logit_model.params[5])*float(data_frame['Nitrous Acid Nitrogen'][i])
    
    Nitric_means = float(logit_model.params[0]) + \
    float(logit_model.params[6])*float(data_frame['Nitric Acid Nitrogen'][i])
    
    Silicic_means = float(logit_model.params[0]) + \
    float(logit_model.params[7])*float(data_frame['Silicic Acid Silicon'][i])
    
    temp_list.append(float(data_frame['Temperature'][i]))
    sal_list.append(float(data_frame['Salinity'][i]))
    oxy_list.append(float(data_frame['Dissolved Oxygen'][i]))
    Phosphate_list.append(float(data_frame['Phosphate Phosphorus'][i]))
    Nitrous_list.append(float(data_frame['Nitrous Acid Nitrogen'][i]))
    Nitric_list.append(float(data_frame['Nitric Acid Nitrogen'][i]))
    Silicic_list.append(float(data_frame['Silicic Acid Silicon'][i]))
    
    #소수점 3째 자리까지 반올림
    temp_means_list.append(round((inverse_logit(temp_means)), 4))
    sal_means_list.append(round((inverse_logit(sal_means)), 4))
    oxy_means_list.append(round((inverse_logit(oxy_means)), 4))
    Phosphate_means_list.append(round((inverse_logit(Phosphate_means)), 4))
    Nitrous_means_list.append(round((inverse_logit(Nitrous_means)), 4))
    Nitric_means_list.append(round((inverse_logit(Nitric_means)), 4))
    Silicic_means_list.append(round((inverse_logit(Silicic_means)), 4))

data = {'Observation Date':data_frame['Observation Date'], 'Temperature': temp_list, 'Temperature_Probability': temp_means_list, 'Salinity':sal_list, 'Salinity_Probability':sal_means_list, 'Dissolved Oxygen':oxy_list, 'Oxygen_Probability':oxy_means_list, 'Phosphate Phosphorus': Phosphate_list, 'Phosphate_Probability': Phosphate_means_list, 'Nitrous Acid Nitrogen':Nitrous_list, 'Nitrous_Probability': Nitrous_means_list, 'Nitric Acid Nitrogen':Nitric_list, 'Nitric_Probability': Nitric_means_list, 'Silicic Acid Silicon':Silicic_list, 'Silicic_Probability': Silicic_means_list}
df = pd.DataFrame(data)

#Nan행 삭제
data_edit = df.dropna()

data_edit.to_csv('result03-4.csv', index=False)

print(data_edit.head())
