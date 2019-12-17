from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve  # 추가

# 저장 폴더를 생성
try:
    if not (os.path.isdir("image")):
        os.makedirs(os.path.join("image"))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

# 요일별 웹툰영역 추출하기
data1_list = soup.findAll("div", {"class": "col_inner"})
# pprint(data1_list)

# 전체 웹툰 리스트
li_list = []
for data1 in data1_list:
    # 제목+썸내일 영역 추출
    li_list.extend(data1.findAll("li"))  # 해당 부분을 찾아 li_list와 병합
# pprint(li_list)

# 각각 썸네일과 제목 추출하기
for li in li_list:
    img = li.find("img")
    title = img["title"]
    img_src = img["src"]
    # print(title,img_src)
    title = re.sub("[^0-9a-zA-Zㄱ-힗]", "", title)  # 해당 영역의 글자가 아니 것은 ''로 치환시킨다.
    urlretrieve(img_src, "./image/" + title + ".jpg")  # 주소, 파일경로+파일명+확장자

