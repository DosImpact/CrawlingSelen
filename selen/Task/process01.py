"""
페이스북 로그인 구현 | 그룹사이트에서 사람들 정보 파싱 -> 번호 및 href

config 파일만 건드리면 됨. 주소,아이디,비번,맴버수,출력파일명 만!!
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import csv

# Config -------------------------------------------
FACEBOOk_URL = "https://www.facebook.com/groups/521003517969832/members/"
EMAIL = "happyaphappy@gmail.com"
PASSWORD = "Fahappy5386!!"
MEMBER_COUNT = 29072
OUTPUT_FILE_NAME = "pro1_Greenstyle.csv"
# -------------------------------------------
# https://www.facebook.com/groups/Patternsforpiratesgroup/
# https://www.facebook.com/groups/PDFPatternSalesandPromotions/
# https://www.facebook.com/groups/sewsweetnessfans/
# https://www.facebook.com/groups/PDFellieandmacsewingpattern/
# https://www.facebook.com/groups/277215386008895/
# https://www.facebook.com/groups/582456251788674/
# https://www.facebook.com/groups/521003517969832/
# https://www.facebook.com/groups/MBJMgroup/#

TIEMINTERVAL = 2
# -------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get(FACEBOOk_URL)
time.sleep(TIEMINTERVAL)
f = open(OUTPUT_FILE_NAME, "w", encoding="utf-16")
wf = csv.writer(f)
# 로그인 파트 -------------------------------------------
email = driver.find_element_by_css_selector("#email")
email.send_keys(EMAIL)
password = driver.find_element_by_css_selector("#pass")
password.send_keys(PASSWORD)
loginbtn = driver.find_element_by_css_selector("#loginbutton")
webdriver.ActionChains(driver).click(loginbtn).perform()
# -------------------------------------------

time.sleep(TIEMINTERVAL)
html = driver.find_element_by_tag_name("html")

content_pointer = 1  # 2번째 부터 크롤링 시작 (나는 제외)
content_ram = []
# 그룹원 href 크롤링 파트 -------------------------------------------
loop, leng = True, 0
while loop and leng < MEMBER_COUNT:
    try:
        for i in range(20):
            html.send_keys(Keys.PAGE_DOWN)
        rows = driver.find_elements_by_css_selector(
            "div.lists  div.fbProfileBrowserList.fbProfileBrowserListContainer ul > div"
        )
        leng = len(rows)
        print(f"인물프로필 갯수 : {leng}")

        while content_pointer < leng - 2:
            content_pointer += 1
            content_a = rows[content_pointer].find_element_by_css_selector("a")
            content_a_name = rows[content_pointer].find_element_by_css_selector(
                "div a")
            content_href = content_a.get_attribute("href")
            content_name = content_a_name.get_attribute("title")
            #print(f"[{content_pointer}] 이름 : {content_name} 링크 : {content_href}")
            wf.writerow([content_pointer, content_name, content_href])
    except TimeoutException:
        loop = False
# -------------------------------------------
# driver.quit()
