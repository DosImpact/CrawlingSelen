from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random, time, os, math

start_time = time.time()


def process(url, userAgent):
    chromedriver = "chromedriver"
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument("user-agent=" + userAgent)
    # options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    driver = webdriver.Chrome(chromedriver, options=options)

    delayTime = random.random() * 10 + random.random() * 100 + 5
    driver.get(url)
    element = driver.find_element_by_tag_name("html")
    for k in range(30):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
    for k in range(30):
        element.send_keys(Keys.PAGE_UP)
        pass
    time.sleep(delayTime)
    print("--User Agnet is End!! {0} --".format(userAgent))
    driver.quit()


def forProcess(url, userAgents):
    for i in userAgents:
        print("--Useragent is Started :: {0} --".format(i))
        process(url, i)


if __name__ == "__main__":
    procs = []
    testurl = "https://www.youtube.com/watch?v=zBcwe316TFE&t=8s"

    f = open("useragent.txt", "r")
    ref = f.readlines()
    filelen = len(ref)
    print("Useragent len : {0}".format(filelen))
    f.close()

    ra1 = 0
    ra2 = math.floor((filelen / 4) * 1)
    ra3 = math.floor((filelen / 4) * 2)
    ra4 = math.floor((filelen / 4) * 3)
    ra5 = math.floor((filelen / 4) * 4)
    print(ra1, ra2, ra3, ra4, ra5)
    # Process 01
    proc = Process(target=forProcess, args=(testurl, ref[ra1:ra2],))
    proc.start()
    procs.append(proc)
    # Process 02
    proc = Process(target=forProcess, args=(testurl, ref[ra2:ra3],))
    proc.start()
    procs.append(proc)
    # Process 03
    proc = Process(target=forProcess, args=(testurl, ref[ra3:ra4],))
    proc.start()
    procs.append(proc)
    # Process 04
    proc = Process(target=forProcess, args=(testurl, ref[ra4:ra5],))
    proc.start()
    procs.append(proc)

    for pr in procs:
        pr.join()

print("ENED --- %s seconds ---" % (time.time() - start_time))
