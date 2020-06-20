# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:41:24 2019

@author: Database_Lab
"""


#sys파일을 불러오겠음.
import sys
#PyQt5사용 
import PyQt5
#QtGui 파일에서 모든 클래스와 함수를 불러옴(GUI)
from PyQt5.QtGui import * 
#QtCore 파일에서 모든 클래스와 함수를 불러옴
from PyQt5.QtCore import *
#QtWidget 파일에서 모든 클래스와 함수를 불러옴(위젯)
from PyQt5.QtWidgets import *
#uic 클래스를 불러오기.
from PyQt5 import uic
import pandas as pd
import statsmodels.api as sm

#데이터 프레임, 중복제거, 리스트 삽입.

#input_data_form.ui라는 PyQt5로 만들어진 ui를 가져오는 역할.
inputDataUI = 'D:\Python3\Python_GUI\input_data_form.ui'

#QDialog를 상속받는 MainDialog 클래스를 새로 선언했다는 의미
#QDialog클래스는 PyQt5.Otwidgets 파일 안에 속한 클래스
class MainDialog(QDialog):
    #클래스 함수의 첫 번째 인수를 self를 써 줘야만 해당 함수를 인스턴스의 함수를 사용.
    #간단히 이 함수를 부르는 객체가 해당 클래스의 인스턴스
    #인스턴스(Instance)란 객체를 소프트웨어에 실체화하면 그것을 인스턴스라고 부름.
    def __init__(self):
        #인스턴스 생성 초기에 변수를 지정해주는 것을 도와주는 __init__함수
        #__init__함수 : 초기화 메서드 혹은 생성자로 불림.
        
        QDialog.__init__(self, None)
        #loadUI(경로,self)는 경로에 있는 ui파일을 불러오는 메소드
        # ui파일이 팝업
        uic.loadUi(inputDataUI, self)
        
        
        #Tap 1 
        #Button
        self.All_Data_read_csv_Pushbutton.clicked.connect(lambda state, button = self.All_Data_read_csv_Pushbutton : self.All_Data_ReadClicked(state, button))
        #Disable TextEdit
        self.All_Data_read_csv_TextEdit.setDisabled(True)
        
        #Tap 2 
        #Disable lineEdit & TextEdit
        self.WaterTempLineEdit.setDisabled(True)
        self.SalinitylineEdit.setDisabled(True)
        self.DissolvedOxygenlineEdit.setDisabled(True)
        self.PhosphatePhosphoruslineEdit.setDisabled(True)
        self.NitrousAcidNitrogenlineEdit.setDisabled(True)
        self.NitricAcidNitrogenlineEdit.setDisabled(True)
        self.SilicicAcidSiliconlineEdit.setDisabled(True)
        
        self.ResultTextEdit.setDisabled(True)
        
        #Able lineEdit
        self.WaterTemp_checkBox.stateChanged.connect(lambda:self.WaterTemp_state(self))
        self.Salinity_checkBox.stateChanged.connect(lambda:self.Salinity_state(self))
        self.DissolvedOxygen_checkBox.stateChanged.connect(lambda:self.DissolvedOxygen_state(self))
        self.PhosphatePhosphorus_checkBox.stateChanged.connect(lambda:self.PhosphatePhosphorus_state(self))
        self.NitrousAcidNitrogen_checkBox.stateChanged.connect(lambda:self.NitrousAcidNitrogen_state(self))
        self.NitricAcidNitrogen_checkBox.stateChanged.connect(lambda:self.NitricAcidNitrogen_state(self))
        self.SilicicAcidSilicon_checkBox.stateChanged.connect(lambda:self.SilicicAcidSilicon_state(self))

        #Reset Button
        self.ResetpushButton.clicked.connect(self.Reset)
        
        #Result Button 
        self.SearchpushButton.clicked.connect(lambda state, button = self.SearchpushButton : self.NumClicked(state, button))
        self.WaterTempLineEdit.setDisabled(True)
          
    #Ui의 'All_Data' Page 
    
    #All_Data를
    def All_Data_ReadClicked(self, state ,button):
        
        #lineEdit에 write한 csv파일을 읽어들임
        #header=0은 해더행 무시한다는 의미. 데이터프레임으로 읽음
        data_frame = pd.read_csv(str(self.All_Data_read_csv_lineEdit.text()), header=0)
        #종속변수로 선언
        dependent_variable = data_frame['On/Off']
        #독립변수로 선언
        independent_variables = data_frame[['Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']]
        #입력변수에 전체 값이 1인 열을 추가
        independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
        #로지스틱 회귀모형에 피팅 (NaN행 무시)
        logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()
        #출력
        #print(logit_model.summary())
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

        #7가지 요소들의 평균 값을 입력시 적조발생 확률
        probability = (inverse_logit(at_means))

        temp_list = []
        sal_list = []
        oxy_list = []
        Phosphate_list = []
        Nitrous_list = []
        Nitric_list = []
        Silicic_list = []
        at_means_list = []

        for i in range(len(data_frame['Observation Date'])):
            at_means = float(logit_model.params[0]) + \
            float(logit_model.params[1])*float(data_frame['Temperature'][i]) + \
            float(logit_model.params[2])*float(data_frame['Salinity'][i]) + \
            float(logit_model.params[3])*float(data_frame['Dissolved Oxygen'][i])
            float(logit_model.params[4])*float(data_frame['Phosphate Phosphorus'][i]) + \
            float(logit_model.params[5])*float(data_frame['Nitrous Acid Nitrogen'][i]) + \
            float(logit_model.params[6])*float(data_frame['Nitric Acid Nitrogen'][i]) + \
            float(logit_model.params[7])*float(data_frame['Silicic Acid Silicon'][i])
    
            temp_list.append(float(data_frame['Temperature'][i]))
            sal_list.append(float(data_frame['Salinity'][i]))
            oxy_list.append(float(data_frame['Dissolved Oxygen'][i]))
            Phosphate_list.append(float(data_frame['Phosphate Phosphorus'][i]))
            Nitrous_list.append(float(data_frame['Nitrous Acid Nitrogen'][i]))
            Nitric_list.append(float(data_frame['Nitric Acid Nitrogen'][i]))
            Silicic_list.append(float(data_frame['Silicic Acid Silicon'][i]))
    
            #소수점 3째 자리까지 반올림
            at_means_list.append(round(((inverse_logit(at_means))), 3))

        data = {'Observation Date':data_frame['Observation Date'], 'Temperature': temp_list, 'Salinity':sal_list, 'Dissolved Oxygen':oxy_list, 'Phosphate Phosphorus': Phosphate_list, 'Nitrous Acid Nitrogen':Nitrous_list, 'Nitric Acid Nitrogen':Nitric_list, 'Silicic Acid Silicon':Silicic_list, 'Probability':at_means_list}
        df = pd.DataFrame(data)

        #Nan행 삭제
        data_edit = df.dropna()
        data_edit.to_csv('result03-3.csv', index=False)
        
        #예측하기
        new_observations = data_frame.ix[data_frame.index.isin(range(30)), independent_variables.columns]
        new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
        y_predicted = logit_model.predict(new_observations_with_constant)
        y_predicted_rounded = [round(score, 2) for score in y_predicted]
        
        self.All_Data_read_csv_TextEdit.setText(str(logit_model.summary())+("\n7가지 요소들의 평균 값을 입력시 적조발생 확률 : %.3f %%" % probability)+'\n'+str(data_edit.head())+'\n'+str(y_predicted_rounded))
        
            
    #Tap2
    
    #체크박스 체크시 LineEdit에 Write 가능하게 만들었습니다.
    #WaterTemp_state라는 함수를 정의
    #setDisable(Ture)는 사용을 못하게 만드는 명령어.
    def WaterTemp_state(self,state):
        if self.WaterTemp_checkBox.isChecked() == True :
            return self.WaterTempLineEdit.setDisabled(False)
        else:
            return self.WaterTempLineEdit.setDisabled(True)    
    def Salinity_state(self,state):        
        if self.Salinity_checkBox.isChecked() == True:
            return self.SalinitylineEdit.setDisabled(False)
        else:
            return self.SalinitylineEdit.setDisabled(True)
    def DissolvedOxygen_state(self,state):    
        if self.DissolvedOxygen_checkBox.isChecked() == True:
            return self.DissolvedOxygenlineEdit.setDisabled(False)
        else:
            return self.DissolvedOxygenlineEdit.setDisabled(True)
    def PhosphatePhosphorus_state(self,state):    
        if self.PhosphatePhosphorus_checkBox.isChecked() == True:
            return self.PhosphatePhosphoruslineEdit.setDisabled(False)
        else:
            return self.PhosphatePhosphoruslineEdit.setDisabled(True)
    def NitrousAcidNitrogen_state(self,state):    
        if self.NitrousAcidNitrogen_checkBox.isChecked() == True:
            return self.NitrousAcidNitrogenlineEdit.setDisabled(False)
        else:
            return self.NitrousAcidNitrogenlineEdit.setDisabled(True)
    def NitricAcidNitrogen_state(self,state):    
        if self.NitricAcidNitrogen_checkBox.isChecked() == True:
            return self.NitricAcidNitrogenlineEdit.setDisabled(False)
        else:
            return self.NitricAcidNitrogenlineEdit.setDisabled(True)
    def SilicicAcidSilicon_state(self,state):    
        if self.SilicicAcidSilicon_checkBox.isChecked() == True:
            return self.SilicicAcidSiliconlineEdit.setDisabled(False0)
        else:
            return self.SilicicAcidSiliconlineEdit.setDisabled(True)
    
    
    #리셋 버튼
    def Reset(self):
        self.WaterTempLineEdit.clear()
        self.SalinitylineEdit.clear()
        self.DissolvedOxygenlineEdit.clear()
        self.PhosphatePhosphoruslineEdit.clear()
        self.NitrousAcidNitrogenlineEdit.clear()
        self.NitricAcidNitrogenlineEdit.clear()
        self.SilicicAcidSiliconlineEdit.clear()
        self.ResultTextEdit.setText("__리셋되었습니다__")
    
    #입력 받은 값을 추출하여 예측하기
    def NumClicked(self, state ,button): 
        value_list1 = [None] * 7
        #내부 초기화에 대비하여 문자열을 저장함.(반복 사용가능)
        if button == self.SearchpushButton:
             
            value_list1[0] = self.WaterTempLineEdit.text()
            value_list1[1] = self.SalinitylineEdit.text()
            value_list1[2] = self.DissolvedOxygenlineEdit.text()
            value_list1[3] = self.PhosphatePhosphoruslineEdit.text()
            value_list1[4] = self.NitrousAcidNitrogenlineEdit.text()
            value_list1[5] = self.NitricAcidNitrogenlineEdit.text()
            value_list1[6] = self.SilicicAcidSiliconlineEdit.text()

        independent_variables2 = [['Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon'],[value_list1[0],value_list1[1],value_list1[2],value_list1[3],value_list1[4],value_list1[5],value_list1[6]]]
        
        dataframe = pd.DataFrame(independent_variables2)
        dataframe.to_csv("D:\Python3\Python_GUI\idd2.csv",header=False,index=False)

        #header=0은 해더행 무시한다는 의미. 데이터프레임으로 읽음
        #data_frame = pd.read_csv('output04.csv', header=0)
        data_frame = pd.read_csv(str(self.input_csv_lineEdit.text()), header=0)
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
        
        at_means = float(logit_model.params[0])
        if value_list1[0] != "":
            at_means = at_means + float(logit_model.params[1])*float(data_frame['Temperature'].mean())
        if value_list1[1] != "":
            at_means = at_means + float(logit_model.params[2])*float(data_frame['Salinity'].mean())
        if value_list1[2] != "":
            at_means = at_means + float(logit_model.params[3])*float(data_frame['Dissolved Oxygen'].mean())
        if value_list1[3] != "":
            at_means = at_means + float(logit_model.params[4])*float(data_frame['Phosphate Phosphorus'].mean())
        if value_list1[4] != "":
            at_means = at_means + float(logit_model.params[5])*float(data_frame['Nitrous Acid Nitrogen'].mean())
        if value_list1[5] != "":
            at_means = at_means + float(logit_model.params[6])*float(data_frame['Nitric Acid Nitrogen'].mean())
        if value_list1[6] != "":
            at_means = at_means + float(logit_model.params[7])*float(data_frame['Silicic Acid Silicon'].mean())

        probability = (inverse_logit(at_means))*100
        print("7가지 요소들의 평균 값을 입력시 적조발생 확률 : %.3f %%" % probability)

        temp_list = []
        sal_list = []
        oxy_list = []
        Phosphate_list = []
        Nitrous_list = []
        Nitric_list = []
        Silicic_list = []
        at_means_list = []
        for i in range(len(data_frame['Observation Date'])):
            at_means = float(logit_model.params[0]) + \
            float(logit_model.params[1])*float(data_frame['Temperature'][i]) + \
            float(logit_model.params[2])*float(data_frame['Salinity'][i]) + \
            float(logit_model.params[3])*float(data_frame['Dissolved Oxygen'][i])
            float(logit_model.params[4])*float(data_frame['Phosphate Phosphorus'][i]) + \
            float(logit_model.params[5])*float(data_frame['Nitrous Acid Nitrogen'][i]) + \
            float(logit_model.params[6])*float(data_frame['Nitric Acid Nitrogen'][i]) + \
            float(logit_model.params[7])*float(data_frame['Silicic Acid Silicon'][i])
    
            temp_list.append(float(data_frame['Temperature'][i]))
            sal_list.append(float(data_frame['Salinity'][i]))
            oxy_list.append(float(data_frame['Dissolved Oxygen'][i]))
            Phosphate_list.append(float(data_frame['Phosphate Phosphorus'][i]))
            Nitrous_list.append(float(data_frame['Nitrous Acid Nitrogen'][i]))
            Nitric_list.append(float(data_frame['Nitric Acid Nitrogen'][i]))
            Silicic_list.append(float(data_frame['Silicic Acid Silicon'][i]))
    
            #소수점 3째 자리까지 반올림
            at_means_list.append(round(((inverse_logit(at_means))*100), 3))

        data = {'Observation Date':data_frame['Observation Date'], 'Temperature': temp_list, 'Salinity':sal_list, 'Dissolved Oxygen':oxy_list, 'Phosphate Phosphorus': Phosphate_list, 'Nitrous Acid Nitrogen':Nitrous_list, 'Nitric Acid Nitrogen':Nitric_list, 'Silicic Acid Silicon':Silicic_list, 'Probability':at_means_list}
        df = pd.DataFrame(data)

        #Nan행 삭제
        data_edit = df.dropna()

        data_edit.to_csv('result03-3.csv', index=False)

        print(data_edit.head())

        #예측하기
        print('======================================================================')
        new_observations = data_frame.ix[data_frame.index.isin(range(30)), independent_variables.columns]
        new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
        y_predicted = logit_model.predict(new_observations_with_constant)
        y_predicted_rounded = [round(score, 2) for score in y_predicted]
        print(y_predicted_rounded)

        #빈칸으로 설정한 data값을 All_Data로 지정함.
        
    
#변수app은 QApplication의 클래스를 상속받음.
#sys.argv는 현재 파일의 절대경로를 반환.
app = QApplication(sys.argv)
#QApplication Class의 __init__의 변수에 파일의 절대경로를 값으로 주어 지금 파일을 실제로 화면에 띄움.
#변수 main_dialog를 만들어서 MainDialog클래스 상속
main_dialog = MainDialog()
#창을 띄우는 역할.
main_dialog.show()
#QApplication.exec_()는 프로그램을 이벤트 루프로 집입시키는 역할.
#이 명령어를 write하지 않으면 창으로 띄워지지 않음. 
app.exec_()

#class information:
    
