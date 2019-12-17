"""

"""
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, csv

# Config -------------------------------------------
PAGE_URL = "https://www.coupang.com/np/search?q=가습기&page=1&channel=recent&rating=0&sorter=scoreDesc&listSize=100"

# -------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
# -------------------------------------------
driver.get(PAGE_URL)
time.sleep(2)
html = driver.page_source
driver.quit()
# -------------------------------------------
f = open("li.csv", "w", encoding="utf-8")
flis = csv.writer(f)

soup = bs(html, "html.parser")
data1 = soup.select("#productList li")
print(f"상품갯수 : {len(data1)}")
for element in data1:
    flis.writerow(element)
# print(data1[0].text)


# 원하는 li만 가져오기

# li가공해서 html로 다시 만들기

exit()
# Config -------------------------------------------
FACEBOOk_URL = "https://www.coupang.com/np/search?q=가습기&page=1&channel=recent&rating=0&sorter=scoreDesc&listSize=100"
EMAIL = "happyaphappy@gmail.com"
PASSWORD = "Fahappy5386!!"
MEMBER_COUNT = 5600
OUTPUT_FILE_NAME = "pro1_PDF.csv"
# -------------------------------------------
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
        for i in range(10):
            html.send_keys(Keys.PAGE_DOWN)
        rows = driver.find_elements_by_css_selector(
            "div.lists  div.fbProfileBrowserList.fbProfileBrowserListContainer ul > div"
        )
        leng = len(rows)
        print(f"인물프로필 갯수 : {leng}")

        while content_pointer < leng - 2:
            content_pointer += 1
            content_a = rows[content_pointer].find_element_by_css_selector("a")
            content_a_name = rows[content_pointer].find_element_by_css_selector("div a")
            content_href = content_a.get_attribute("href")
            content_name = content_a_name.get_attribute("title")
            print(f"[{content_pointer}] 이름 : {content_name} 링크 : {content_href}")
            wf.writerow([content_pointer, content_name, content_href])
    except TimeoutException:
        loop = False
# -------------------------------------------
# driver.quit()
