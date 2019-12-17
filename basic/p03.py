from bs4 import BeautifulSoup as bs
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = bs(html.text, "html.parser")

datas = soup.select("div.list_area div.col li > a")


for data in datas:
    print(data)
    pass
