from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get("https://www.facebook.com/groups/mogaco/")

html = driver.find_element_by_tag_name("html")

content_pointer = 4  # 4번째 부터 크롤링 시작
content_ram = []

feed = driver.find_elements_by_css_selector(
    "div#pagelet_group_mall > div > div._5pcb > div > div"
)
leng = len(feed)
content = feed[18].find_element_by_css_selector(".userContent")
time.sleep(1)
print(content.text)
print(f"게시물 갯수 : {leng}")

time.sleep(1)
driver.quit()
