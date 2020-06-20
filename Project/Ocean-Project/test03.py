#!/usr/bin/env python3 
# 2000~2017년 웹 크롤링
import pandas as pd
from dateutil.parser import parse

df=pd.read_html('http://www.nifs.go.kr/red/news/news_2000.jsp', flavor='html5lib')

df=df[1]

date = []
for month in range(1,12):
    for df_index in df[0]:
        if '{0:d}월'.format(month) in str(df_index):
            date.append(df_index)

date_year = []
for index in date:
    index = "2000년 "+index
    date_year.append(index)

date_replace = []
for index in date_year:
    date_replace.append(index.replace("년","-").replace("월","-").replace("일","").replace(" ",""))

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))
    
date_new = list(set(date_new))

with open("result01.csv", 'w', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")

###############################################################################유해적조X

df=pd.read_html('http://www.nifs.go.kr/red/news/news_2001.jsp', flavor='html5lib')

df=df[0]

date = []
date.append(df[0][1].replace("2001.",""))

for i in range(2,len(df[0])):
    if '.' in str(df[0][i]):
        date.append(df[0][i])
        tmp = str(df[0][i]).split()[0]
    elif '〃' not in str(df[0][i]):
        if str(df[0][i]) != 'nan':
            df_index = tmp + str(df[0][i])
            date.append(df_index)
            
date_year = []
for index in date:
    index = "2001년 "+index
    date_year.append(index)

date_replace = []
for index in date_year:
    date_replace.append(index.replace("년","-").replace(".","-").replace("일","").replace(" ",""))


date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))
    
date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
      
###############################################################################

df=pd.read_html('http://www.nifs.go.kr/red/news/news_2002.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0]:
    if '.' in str(df_index):
        date.append(df_index)
        
date_replace = []
for index in date:
    index = index.replace(". ","-").replace(".","-")
    index = "2002-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        
###############################################################################

df=pd.read_html('http://www.nifs.go.kr/red/news/news_2003.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0]:
    if '월' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2003-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2004.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0]:
    if '.' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(".","-")
    index = "2004-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2005.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0][:-1]:
    if '.' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(".","-").replace(" ","")
    index = "2005-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2006.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0][:-1]:
    if '.' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(".","-").replace(" ","")
    index = "2006-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")    
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2007.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0]:
    if '.' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(".","-").replace(" ","")
    index = "2007-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")         
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2008.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0][:-1]:
    if '.' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(".","-").replace(" ","")
    index = "2008-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        
###############################################################################8월달적조발생X
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2009.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0][:-1]:
    if '.' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(".","-").replace(" ","")
    index = "2009-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2010.jsp', flavor='html5lib')

df=df[1]

date = []
for df_index in df[0][:-1]:
    if '.' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(".","-").replace(" ","")
    index = "2010-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        
###############################################################################적조발생X
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2011.jsp', flavor='html5lib')

df=df[0]

date = []
date.append(df[0][1].replace("2011년 ",""))

for i in range(2, len(df[0])):
    if '월' in str(df[0][i]):
        date.append(df[0][i])

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2011-"+index
    date_replace.append(index)

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")  
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2012.jsp', flavor='html5lib')

df=df[1]

date = []
for month in range(1,12):
    for df_index in df[0]:
        if '{0:d}월'.format(month) in str(df_index):
            date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2012-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")      
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2013.jsp', flavor='html5lib')

df=df[1]

date = []
for month in range(1,12):
    for df_index in df[0]:
        if '{0:d}월'.format(month) in str(df_index):
            date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2013-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
          
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2014.jsp', flavor='html5lib')

df=df[2]

date = []
for df_index in df[0]:
    if '월' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2014-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")        
        
###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2015.jsp', flavor='html5lib')

df=df[2]

date = []
for df_index in df[0]:
    if '월' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2015-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")     

###############################################################################
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2016.jsp', flavor='html5lib')

df=df[2]

date = []
for df_index in df[0]:
    if '월' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2016-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")    

###############################################################################유해적조X
        
df=pd.read_html('http://www.nifs.go.kr/red/news/news_2017.jsp', flavor='html5lib')

df=df[0]

date = []
for df_index in df[0]:
    if '월' in str(df_index):
        date.append(df_index)

date_replace = []
for index in date:
    index = index.replace(". ","-").replace("월","-").replace("일","").replace(" ","")
    index = "2017-"+index
    date_replace.append(index)  

date_new = []
for index in date_replace:
    date_new.append(parse(index).strftime('%Y-%m-%d'))

date_new = list(set(date_new))

with open("result01.csv", 'a', newline='', encoding='utf-8') as csv_out_file:
    for index in date_new:    
        csv_out_file.write(index+"\n")
        

#날짜 순으로 정렬         
df1 = pd.read_csv("result01.csv", header=None)
df1 = df1.sort_values(by=0, ascending=True)
df1.to_csv('result01.csv', sep=',', encoding='utf-8', index=False, header=None)

