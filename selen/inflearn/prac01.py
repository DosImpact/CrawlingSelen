"""
 파이썬 홈페이지를 가져와, html태그 css selector로 요소를 찾고, 키를 입력
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get("http://www.python.org")

html = driver.find_element_by_tag_name("html")
anya = driver.find_element_by_css_selector(
    "#content > div > section > div:nth-child(1) > div.small-widget.jobs-widget.last > h2"
)
print(vars(html))
print(dir(html))
for i in range(10):
    html.send_keys(Keys.PAGE_DOWN)

print(anya.text)
