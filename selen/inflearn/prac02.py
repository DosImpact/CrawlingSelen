from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome("chromedriver")
driver.get("https://www.youtube.com/watch?v=e3rAUHNHqZA&list=UUI0MH1C8JwvLumquXyDqSHg")

time.sleep(2)

search = driver.find_element_by_xpath(
    '//*[@id="publisher-container"]/div/yt-formatted-string'
)
time.sleep(2)

loginButton = driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
loginButton.send_keys(Keys.ENTER)

time.sleep(2)

logininput = driver.find_element_by_xpath('//*[@id="identifierId"]')
logininput.send_keys("ypd03008")
time.sleep(1)
logininput.send_keys(Keys.ENTER)

time.sleep(2)

passwordinput = driver.find_element_by_xpath(
    '//*[@id="password"]/div[1]/div/div[1]/input'
)
passwordinput.send_keys("Godud5386!!")
time.sleep(1)
passwordinput.send_keys(Keys.ENTER)

time.sleep(2)


print("스크롤링~ 및 동적로딩")
element = driver.find_element_by_tag_name("html")
for i in range(300):
    element.send_keys(Keys.PAGE_DOWN)

print("댓글창 찾기 과정 .. ")
time.sleep(1)


print("공개 댓글 추가.")
rewordinput = driver.find_element_by_xpath('//*[@id="simplebox-placeholder"]')
# rewordinput.click
rewordinput.send_keys(Keys.ENTER)

time.sleep(1)
print("공개 댓글 입력")
rewordinput = driver.find_element_by_xpath('//*[@id="contenteditable-textarea"]')
rewordinput.click
rewordinput.send_keys(
    "반원 생활님의 강의를 듣고 자동으로 댓글쓰는 봇 입니다. ! 강의 잘 듣고 있습니다. 문제시 삭제하겠습니다. !! "
)
time.sleep(1)

print("댓글 클릭하기")
rewordinput = driver.find_elements_by_css_selector("#submit-button > a > paper-button")
print("#submit-button > a > paper-button ", len(rewordinput), rewordinput[0].text)
# rewordinput[0].click
rewordinput[0].send_keys(Keys.ENTER)

time.sleep(1)


# 로그인 버튼의 xpath : //*[@id="buttons"]/ytd-button-renderer/a
# 아이디 입력창의 xpath : //*[@id="identifierId"]
# 비밀 번호 입력창의 xpath : //*[@id="password"]/div[1]/div/div[1]/input
# 공개 댓글 입력창의 동적로딩을 위한 xpath : //*[@id="simplebox-placeholder"]
# 공개 댓글 입력창의 xpath : //*[@id="contenteditable-textarea"]
# 댓글을 달면 -> 파란 버튼이 동적 활성화 // 그중 31 번째 버튼임
"""
scroll_from_element(on_element, xoffset, yoffset)
Touch and scroll starting at on_element, moving by xoffset and yoffset.
 
Args:  
on_element: The element where scroll starts.
xoffset: X offset to scroll to.
yoffset: Y offset to scroll to.
 
예시 ) ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
 
"""

