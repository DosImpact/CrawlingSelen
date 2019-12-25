"""
CSV 이어서 쓰기 모드
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import csv
import random

# Config -------------------------------------------
FACEBOOk_URL = "https://www.facebook.com/groups/indiera/members/"
TIEMINTERVAL = 3
IDINTERVALPERR = 60  # 90개의 게시물을 보면 아이디를 체인지 합니다.
INPUT_FILE_NAME = "pro1_Greenstyle.csv"
INPUT_START_LINE = 304  # pk보다 하나 적게 이어서 시작!!
OUTPUT_FILE_NAME = "pro2_Greenstyle.csv"
HOUSE_IMG_CLASS = "sx_784d4a"  # 페이스북은 매일매일 CLASS이름을 바꿔주나봐.. 이것도 체킹해야됨..
# _3-90 _8o _8s lfloat _ohe img sp_2LodHPNm148_2x sx_784d4a
EMAIL_LIST = [
    "79215678876",
    "79916771956",
    "79219881428",
    "tkdwls4152@naver.com",
    "o19941025@gmail.com",
]
PASSWORD_LIST = [
    "5*5z6b*F(",
    "e$QG1F85a",
    "64yHn4&kx",
    "!girintkdwls4152",
    "dla2068"
]
# private Config -------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
output_format = []
NOWIDPOINTER = 0
EMAIL = "79219881428"
PASSWORD = "64yHn4&kx"
IDLIST = []
# csv FileRead--------------------------------------------
csvfile = open(INPUT_FILE_NAME, "r", encoding="utf-16")
csvfilerows = csv.reader(csvfile)
urls = []
for row in csvfilerows:
    if len(row) == 0:
        continue
    # print(row)
    urls.append([row[0], row[1], row[2]])
csvfile.close()
# -------------------------------------------

# 로그인 파트 -------------------------------------------


def changeUser():
    global NOWIDPOINTER
    global EMAIL
    global PASSWORD
    if(NOWIDPOINTER >= len(EMAIL_LIST) - 1):
        NOWIDPOINTER = 0
    email = EMAIL_LIST[NOWIDPOINTER]
    password = PASSWORD_LIST[NOWIDPOINTER]
    print(f"change user to {email} & {password}")
    EMAIL = email
    PASSWORD = password
    NOWIDPOINTER += 1


def login():
    global driver
    changeUser()
    driver.close()
    driver = webdriver.Chrome(os.path.join(BASE_DIR, "chromedriver.exe"))
    driver.get(FACEBOOk_URL)  # 로그인페이지로 이동됨.
    email = driver.find_element_by_css_selector("#email")
    email.send_keys(EMAIL)
    password = driver.find_element_by_css_selector("#pass")
    password.send_keys(PASSWORD)
    loginbtn = driver.find_element_by_css_selector("#loginbutton")
    webdriver.ActionChains(driver).click(loginbtn).perform()


login()
# -------------------------------------------


# csv FileWrite--------------------------------------------
csvfile = open(OUTPUT_FILE_NAME, "a", encoding="utf-16")
csvfilerows = csv.writer(csvfile)


print(
    f"cvs href -> profile 수집 시작 , profile 수 : {len(urls)}, ID변경간격: {IDINTERVALPERR}")
# crawl each person-------------------------------------------
counter = 0
for i in range(INPUT_START_LINE, len(urls) - 1, 1):
    counter += 1
    driver.get(urls[i][2])
    time.sleep(random.randint(5, 15))
    urls[i].pop()
    try:
        element = WebDriverWait(driver, TIEMINTERVAL + 2).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#profile_timeline_intro_card",)
            )
        )
        profile = driver.find_element_by_css_selector(
            "#profile_timeline_intro_card")
        house = profile.find_element_by_css_selector(
            f"i.{HOUSE_IMG_CLASS} + div")
        house_text = house.text
        urls[i].extend([house_text])

        profile_lists = profile.find_elements_by_css_selector("li li")
        for list in profile_lists:
            urls[i].extend([list.text])

    except TimeoutException:  # 블락된 경우
        print("TIME OUT EXCEPTION", urls[i])
        csvfilerows.writerow(urls[i])
        counter = 0
        login()
        continue
    except NoSuchElementException:  # 거주지 정보가 없는 경우
        print("No Such Element Exception", urls[i])
        csvfilerows.writerow(urls[i])
        continue

    print(urls[i])
    csvfilerows.writerow(urls[i])
    #time.sleep(random.randint(10, 50))
    if(counter >= IDINTERVALPERR):
        counter = 0
        login()

csvfile.close()
