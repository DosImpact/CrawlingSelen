from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
driver.get("https://news.v.daum.net/v/20191215123504503")

time.sleep(3)
html = driver.find_element_by_tag_name("html")

loop, count = True, 0
while loop and count < 10:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#alex-area > div > div > div > div.cmt_box > div.alex_more > a",
                )
            )
        )
        more_button = driver.find_element_by_css_selector(
            "#alex-area > div > div > div > div.cmt_box > div.alex_more > a"
        )
        webdriver.ActionChains(driver).click(more_button).perform()
        count += 1
        time.sleep(1)
    except TimeoutException:
        loop = False

time.sleep(5)
data1 = driver.find_elements_by_css_selector("ul.list_comment li")
print(len(data1))

driver.quit()
