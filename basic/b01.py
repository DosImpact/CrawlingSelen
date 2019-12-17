from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get("https://search.naver.com/search.naver?query=날씨")
print(html.text)

soup = bs(html.text, "html.parser")

data1 = soup.find(
    "div", {"class": "detail_box"}
)  # find 한다. 인자 : 태그,클리스와 클래스 값 -> 하나의HTML뭉텅이로 나온다.
# pprint(data1)

data2 = data1.findAll("dl")  # dd태그부분을 모두 찾아서 리스트로 반환 한다.
# pprint(data2)

# print(data2)  # 여러가지 정보가 있어서 그렇지
# print(data2[0].text)  # 텍스트로만 뿌리면 살만 발라짐.
# 미세먼지 18㎍/㎥좋음 초미세먼지 13㎍/㎥좋음 오존지수 0.012ppm좋음

# 또는 다른 방법도 있음
data1 = soup.select(".indicator")
# print(data1[0].text)
