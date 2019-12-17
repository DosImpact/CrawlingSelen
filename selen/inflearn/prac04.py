""" 네이버 웹툰 제목 크롤링 | csv 저장 """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os, time, csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get("https://comic.naver.com/webtoon/weekday.nhn")


datas = driver.find_elements_by_css_selector("div.list_area li a.title")
f = open("output.csv", "w", encoding="utf-16", newline="")
wr = csv.writer(f)
for num, data in enumerate(datas):
    title = data.get_attribute("title")
    print(f"[{num}] : {title}")
    wr.writerow([num, title])

driver.quit()
