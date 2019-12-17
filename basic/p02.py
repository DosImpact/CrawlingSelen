from bs4 import BeautifulSoup as bs
import requests

html = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
soup = bs(html.text, "html.parser")

datas = soup.select("table.list_ranking a")

for data in datas:
    print(data.text)
