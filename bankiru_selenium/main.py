from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import random
import os

headers = []
bodies = []
dates = []

# create useragent class
useragent = UserAgent()

# options
options = webdriver.ChromeOptions()

# set rotate useragent
options.add_argument(f'user-agent={useragent.random}')

# set proxy
#options.add_argument('--proxy-server=103.68.194.126:8888')

# driver
driver = webdriver.Chrome(
    executable_path='C:\\Users\\79771\\PycharmProjects\\bankiru_selenium\\chromedriver.exe',
    options=options
)

url = 'https://www.banki.ru/services/responses/bank/sberbank/?page=1'
url_test_useragent = 'https://whatmyuseragent.com/'
url_test_webdriver = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'
url_ip_test = 'https://2ip.ru/'
driver.maximize_window()

# pages range - list comprehension
pages = ['https://www.banki.ru/services/responses/bank/sberbank/?page='+str(x) for x in range(1, 256)]

# test proxy
# driver.get(url_ip_test)
# time.sleep(15)

try:
    for q in pages:
        driver.get(q)
    # for finding elements in html file
    # # with open('banki.html', 'w', encoding="utf-8") as f:
    # #     f.write(driver.page_source)
    # # header = driver.find_element(By.CLASS_NAME, 'header-h3')
    # # print(header.get_attribute("innerHTML"))
    # #

        header = driver.find_elements(By.CLASS_NAME, 'header-h3')
        for i in header:
            headers.append(i.get_attribute("innerHTML"))

        body = driver.find_elements(By.CLASS_NAME, 'responses__item__message')
        for j in body:
            if 'Читать далее' not in j.get_attribute("innerHTML"):
                bodies.append(j.get_attribute("innerHTML").replace('\n', '')\
                              .replace('\t', '').replace('<br>', '').replace('&nbsp;', '')\
                              .replace('<strong>', '').replace('</strong>', '')\
                              .replace('\u200b', '').replace('<li>', '').replace('</ul>', '')\
                              .replace('</li>', '').replace('<ul class="decoda-list">', '')\
                              .strip())

        date = driver.find_elements(By.CLASS_NAME, 'display-inline-block')
        for y in date:
                dates.append(y.get_attribute("innerHTML"))

# save appeals in txt file
    with open('appeals3.txt', 'w', encoding="utf-8") as file:
        for p in range(len(bodies)):
            file.write(headers[p] + '\n')
            file.write(bodies[p] + '\n')
            file.write(dates[p] + '\n')
            file.write('\n')

# closing web-driver
finally:
    driver.close()
    driver.quit()