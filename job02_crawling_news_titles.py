from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as Chrome_options
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome import ChromeDriverManager
import time
import pandas as pd

from job01_crawling_headline import category

options = Chrome_options()
options.add_argument("lang=ko_KR")
# options.add_argument("headless")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

my_section = 0 # 0 정치 1 경제 2 사회 3문화 4 세계 5 IT

url = "https://news.naver.com/section/10{}".format(my_section) # 100 : Politics , 101 : ....
driver.get(url)
button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]'

# 더보기 클릭
for q in range(50):
    driver.find_element(By.XPATH, button_xpath).click()
    time.sleep(0.5)

# while True:
#     try:
#         button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]'
#         driver.find_element(By.XPATH, button_xpath).click()
#         time.sleep(0.1)
#     except:
#         break

# 더보기 클릭 끝


time.sleep(1)
titles_tags = driver.find_elements(By.CLASS_NAME,'sa_text_strong')

titles = []

for title_tag in titles_tags:
    titles.append(title_tag.text)

df_titles = pd.DataFrame(titles, columns=['title'])
df_titles['category'] = category[my_section] # 섹션 구분
print(df_titles.head())
df_titles.info()
df_titles.to_csv('news_titles_{}.csv'.format(category[my_section]), index=False)


# for i in range(1, 70):
#     for j in range(1,7):
#         try:
#             title_xpath = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(i,j)
#             title = driver.find_element(By.XPATH, title_xpath).text
#             print(title)
#         except:
#             print(i,j)
#             continue


