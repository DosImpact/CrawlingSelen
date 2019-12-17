from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#월요웹툰영역 추출하기
data1=soup.find('div',{'class':'col_inner'})
#pprint(data1)

#제목 포함영역 추출하기
data2=data1.findAll('a',{'class':'title'})
# pprint(data2)

#텍스트만 추출 1
# title_list = []
# for t in data2:
#     title_list.append(t.text)
#
# pprint(title_list)

#텍스트만 추출 2
title_list = [t.text for t in data2]
# 3항 인데.. 리스트형 테이터 data2에서 하나씩 순회하는데, t라고 포인팅 할께. 거기서 t.text를 리스트에 담을꺼야
pprint(title_list)
#1.3.2 네이버 웹툰제목 가져오기 2
from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#요일별 웹툰영역 추출하기
data1_list=soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

#전체 웹툰 리스트
week_title_list = []

for data1 in data1_list:
   #제목 포함영역 추출하기
   data2=data1.findAll('a',{'class':'title'})
   # pprint(data2)

   #텍스트만 추출 2
   title_list = [t.text for t in data2] #여기서 이미 리스트를 만들었어.
   # pprint(title_list)
   #결정 => 1.리스트를 리스트의 원소로 넣을것인가 2. 리스트를 그냥 1차원 리스트로 연장을 할건가.
   week_title_list.extend(title_list) #단순하게 값을 추가해 1차원으로 만들려면 extend
   # week_title_list.append(title_list) #요일별로 나눠 2차원 리스트를 만들려면 append

pprint(week_title_list)
