from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys

#Headless
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# # 혹은 options.add_argument("--disable-gpu")
# ######################


## setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성 # Headless 를 위해 chrome_options=options 추가
driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')#, chrome_options=options)
driver.implicitly_wait(3) ## 암묵적으로 웹 자원을 (최대) 3초 기다리기
## Login
driver.get('https://www.facebook.com/') ## 로그인 URL로 이동하기
driver.find_element_by_name('email').send_keys('rlawoals534@hanmail.net') ## 값 입력
driver.find_element_by_name('pass').send_keys('nec654321!')
driver.find_element_by_xpath(
    '//*[@id="loginbutton"]'
    ).click() ## 로그인 버튼클릭하기

driver.get('https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=ZmVlZGJhY2s6MjkzNDEyODUyNjYxMTk4OQ%3D%3D&av=100001075674704') ## target 계정  URL로 이동하기

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #ESC 크롬 알림 권한 창 때문


html = driver.page_source ## 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
# notices = soup.select('div.p_inr > div.p_info > a > span')
# print(html)
# user = soup.select('#u_0_m > #globalContainer > #content > #js_1 > div._4bl7 _4k2o > ul.uiList _5i_n _4kg _6-h _6-j _6-i > div._5i_p > ul.uiList _4kg > div._5i_q > div.clearfix > div._8u _42ef > div._5i_t > div._6a._5j0c > div._6a _6b > div._5j0e fsl fwb fcb > a._5i_s _8o _8r lfloat _ohe ')
driver.find_element_by_xpath('//*[@id="reaction_profile_pager1"]/div/a').click()
driver.implicitly_wait(20) ## 암묵적으로 웹 자원을 (최대) 3초 기다리기

html1 = driver.page_source ## 페이지의 elements모두 가져오기
soup1 = BeautifulSoup(html1, 'html.parser') ## BeautifulSoup사용하기
print(html1)
user = soup1.select('#reaction_profile_browser1 > li > div > div > div > div._6a._5j0c > div > div > a')

# print(user)
    