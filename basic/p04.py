from bs4 import BeautifulSoup as bs
import requests, os, re
from urllib.request import urlretrieve

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = bs(html.text, "html.parser")
html.close()

try:
    if not os.path.isdir("./images"):
        os.mkdir(os.path.join("./images"))
except OSError as e:
    print("Error 폴더생성 실패!!")
    exit()

datas = soup.select("div.list_area li div.thumb a img")
for data in datas:
    title = data["title"]
    src = data["src"]
    title = re.sub("[^0-9a-zA-Zㄱ-힗]", "", title)  # 해당 영역의 글자가 아니 것은 ''로 치환시킨다.
    urlretrieve(src, f"./images/{title}.jpg")  # 주소, 파일경로+파일명+확장자
    # print(f"title: {title}\tsrc: {src} ")
    # urlretrieve(title, f"./images/{src}.jpg")
