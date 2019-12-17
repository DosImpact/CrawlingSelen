"""
페이스북 로그인 구현
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, csv

# Config -------------------------------------------
EMAIL = "ypd03008@naver.com"
PASSWORD = "Fadud5386!!"
TIEMINTERVAL = 2
# -------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get("https://www.facebook.com/groups/mogaco/members/")
time.sleep(TIEMINTERVAL)

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

loop, leng = True, 0
while loop and leng < 100:
    try:
        for i in range(5):
            html.send_keys(Keys.PAGE_DOWN)
        rows = driver.find_elements_by_css_selector(
            "div.lists  div.fbProfileBrowserList.fbProfileBrowserListContainer > ul > div > a"
        )
        leng = len(rows)
        print(f"인물프로필 갯수 : {leng}")
        # 현재까지 모인 게시물에서 내용부분만 발췌
        print(rows[3])
        print(rows[3].text)
        print(rows[3].get_attribute("src"))

        time.sleep(1)
    except TimeoutException:
        loop = False

# driver.quit()
