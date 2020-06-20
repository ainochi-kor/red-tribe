#!/usr/bin/env python3
# 헤더행 제거, 날짜 형식 변환 (파이썬)

#parse 파싱하기 위한 데이터 같음..
import csv
from dateutil.parser import parse

#파일을 미리 지정해준다.
input_file = 'output01.csv'
output_file = 'output02.csv'

#파일 부분을 input_file은 읽어오는 부분이다. newline=''아닐시 csv 파일 객체
#문제가 생길 수 있음.
with open(input_file, 'r', newline='', encoding='cp949') as csv_in_file:
    with open(output_file, 'w', newline='', encoding='cp949') as csv_out_file:
        #csv 객체로 읽어와서 읽어야 함.
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        
        #헤더 부분을 따로 저장했습니다.
        header = next(filereader)
        #filewriter.writerow(header)
        
        #filereader의 부분을 하나씩 돌려가면서 읽습니다.
        for row_list in filereader:
            #obseration_date를 row_list 파일 읽은 부분의 데이터를 하나씩 정제함.
            obseration_date = row_list[0]
            #datestr은 문자열을 일부 형식으로 만들어서 나눈것.. 기본 자료를 파싱하는것.
            datestr = parse(obseration_date).strftime('%Y-%m-%d')
            #row_list를 row_list에 넣어서 계속 반복...
            row_list[0] = datestr
            
            filewriter.writerow(row_list)
