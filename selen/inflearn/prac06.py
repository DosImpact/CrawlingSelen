from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get("https://www.facebook.com/groups/mogaco/")

html = driver.find_element_by_tag_name("html")

content_pointer = 3  # 4번째 부터 크롤링 시작
content_ram = []
f = open("output.csv", "w", encoding="utf-16")
wf = csv.writer(f)
loop, leng = True, 0
while loop and leng < 100:
    try:
        for i in range(5):
            html.send_keys(Keys.PAGE_DOWN)
        feed = driver.find_elements_by_css_selector(
            "div#pagelet_group_mall > div > div._5pcb > div > div"
        )
        leng = len(feed)
        print(f"게시물 갯수 : {leng}")
        # 현재까지 모인 게시물에서 내용부분만 발췌
        while content_pointer < leng - 5:
            content_pointer += 1
            content = feed[content_pointer].find_element_by_css_selector(".userContent")
            content_ram.extend(content.text)
            print(f"[{content_pointer}] 게시물 콘텐츠 : {content.text}")
            wf.writerow([content_pointer, content.text])

        time.sleep(1)
    except TimeoutException:
        loop = False

driver.quit()
