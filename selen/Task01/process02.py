"""

"""
from bs4 import BeautifulSoup as bs
import os, time, csv

f = open("li.csv", "r", encoding="utf-8")
fcsvReader = csv.reader(f)
lis = []
target_html = """"""

for e in fcsvReader:
    if len(e) == 0:
        continue
    lis.append(e)
    target_html += str(e)

soup = bs(target_html, "html.parser")

# --------------------------------------------------------------------------------
# name = soup.select("div.name")  ##productList li div.name

content = []
# 결국 핵심내용만 CSV로 만든다음에, js로 처리해야겠다.아니면 일딴 최소로 줄여 보자.
# 순위 , 사진, (로켓배송), 이름,(원래가격),(할인률) 가격,

items_a = soup.select("a")  # productList li a
for i in range(0, 3, 1):
    content_ele = []

    pk = i + 1  # 순위
    img = items_a[i].select_one("dt.image img")  # 사진
    rocket = items_a[i].select_one("div.name")  # (로켓배송)
    name = items_a[i].select_one("div.name")  # 이름
    original_price = items_a[i].select_one("dspan.price-info del")  # (원래가격)
    saleper = items_a[i].select_one("span.price-info span")  # (할인률)
    price = items_a[i].select_one("em.sale strong")  # 가격

    content_ele.append(pk)
    content_ele.append(img)
    if rocket == "":
        content_ele.append(" ")
    else:
        content_ele.append(rocket)
    content_ele.append(name)
    if original_price == "":
        content_ele.append(" ")
    else:
        content_ele.append(original_price)
    if saleper == "":
        content_ele.append(" ")
    else:
        content_ele.append(saleper)
    content_ele.append(price)
    print(content_ele)
    content.append(content_ele)
