# 페이스북 그룹 페이지 크롤링 ( deprecated update )

```
# 페이스북 로그인 기능

# 페이스북의 사람들을 스크롤를 내리면서 크롤링 합니다. 사람들의 url 주소 수집.

# url에 접속하여 데이터를 수집.

# 엑셀로 output 합니다.

# bs 및 request 기본 익히기
```
# 환경설치

```
pip install beautifulSoup
pip install requests
pip install selenium
```

# bs 및 request 기본 익히기 1.1

- html 페이지를 request

```
from bs4 import BeautifulSoup as bs #
import requests #

html = requests.get("https://search.naver.com/search.naver?query=날씨")
pprint(html.text)
soup = bs(html.text, "html.parser")
html.close()
```

- html내용 파싱하기

```
#find함수사용하기.
data1 = soup.find(
    "div", {"class": "detail_box"}
)  # find 한다. 인자 : 태그,클리스와 클래스 값 -> 하나의HTML뭉텅이로 나온다.

#findAll함수 사용하기.
data2 = data1.findAll("dl")  # dd태그부분을 모두 찾아서 리스트로 반환 한다.
print(data2[0].text)  # 텍스트로만 뿌리면 살만 발라짐.

#select css 선택자 사용하기.
data1 = soup.select(".indicator")

```

- 리스트에서 필요한 내용만 모아서 -> 빠르게 리스트 만들기

```
week_title_list = []
for data1 in data1_list:
   data2 = data1.findAll('a',{'class':'title'})
   title_list = [t.text for t in data2] #여기서 이미 리스트를 만들었어.
   week_title_list.extend(title_list) #단순하게 값을 추가해 1차원으로 만들려면 extend

```

# selenium 기본 익히기

# selenium 기본 익히기 1.1

- 파이썬 홈페이지를 가져와, html태그 css selector로 요소를 찾고, 키를 입력

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get("http://www.python.org")

html = driver.find_element_by_tag_name("html")
anya = driver.find_element_by_css_selector(
    "#content > div > section > div:nth-child(1) > div.small-widget.jobs-widget.last > h2"
)
print(vars(html))
print(dir(html))
for i in range(10):
    html.send_keys(Keys.PAGE_DOWN)

print(anya.text)

```

# 엑셀 파일 읽기 쓰기

# 엑셀 파일 쓰기 1.1

- 간단하게 csv 입력

```python
import  csv

f = open("output.csv", "w", encoding="utf-16", newline="")
wr = csv.writer(f)
for num, data in enumerate(datas):
    title = data.get_attribute("title")
    print(f"[{num}] : {title}")
    wr.writerow([num, title])
```

# 엑셀 파일 읽기 1.2

- 간단하게 csv 읽어오기 한줄씩

```python
import csv

f = open("output.csv", "r", encoding="utf-16")
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close()

```
