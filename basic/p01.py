from bs4 import BeautifulSoup as bs
import requests

html = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
soup = bs(html.text, "html.parser")

data1 = soup.find("table", {"class": "list_ranking"})
# print(data1)

data2 = data1.findAll("a")
print(data2)
for data in data2:
    print(data.text)
