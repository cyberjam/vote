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
driver.find_element_by_name('email').send_keys('') ## 값 입력
driver.find_element_by_name('pass').send_keys('')
driver.find_element_by_xpath(
    '//*[@id="loginbutton"]'
    ).click() ## 로그인 버튼클릭하기

driver.get('https://www.facebook.com/jysida') ## target 계정  URL로 이동하기

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #ESC 크롬 알림 권한 창 때문



# #########################################
# # 스크롤 가장 하단으로 
# SCROLL_PAUSE_TIME = 0.5

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# ##########################################


html = driver.page_source ## 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') ## BeautifulSoup사용하기
# notices = soup.select('div.p_inr > div.p_info > a > span')
# print(html)
urls = soup.select('form.commentable_item > div._4299 > div._78bu > div._68wo > div._3vum > div._66lg > a ')
# print(urls)
# test = soup.select('div._5pcb _4b0l _2q8l > div._4-u2 mbm _4mrt _5jmm _5pat _5v3q _7cqq _4-u8 > div._3ccb > div._5pcr userContentWrapper > div.commentable_item > div._4299 > div._78bu > div._68wo > div._3vum > div._66lg > a')

# test = soup.select('#u_fetchstream_3_6 > div._4299 > div._78bu > div._68wo > div._3vum > div._66lg > a')
# test = soup.select('div._5pcb _4b0l _2q8l > div._4-u2 mbm _4mrt _5jmm _5pat _5v3q _7cqq _4-u8 > div._3ccb')
# '#u_0_2l'
# print(test)

days = soup.select('abbr._5ptz > span ')

dayss=[]
urll=[]
users = []

for day in days:
    dayss.append(day.text) # 나중에 시간지정을 위해 
    # _5j0e fsl fwb fcb
    
name_list = [] # 좋아요 누른 사람들. 목록 중복 제거 안함


for url in urls:
    urll.append(url.get('href'))
    driver.get('https://www.facebook.com'+ url.get('href')) ## 로그인 URL로 이동하기
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    html2 = driver.page_source
    
    soup2 = BeautifulSoup(html2, 'html.parser')

    try:
        print("hi")
        driver.find_element_by_xpath('//*[@id="reaction_profile_pager1"]/div/a').click() # ' ' " " 구분 
	# driver.find_element_by_xpath('//*[@id="loginbutton"]').click() ## 로그인 버튼클릭하기
        html2 = driver.page_source
        
        soup2 = BeautifulSoup(html2, 'html.parser')
    except:
        print("except")
        pass



    # for i in range(3)
    # driver.find_element_by_xpath(
    # '//*[@id="reaction_profile_pager'+str(i) +'"]/div/a'
    # ).click() ## 로그인 버튼클릭하기



    user = soup2.select('#reaction_profile_browser1 > li > div > div > div > div._6a._5j0c > div > div > a')
    # 가져오는 html 과 실제 html이 다르기 때문에 가져오는 html을 beautiful로 정렬하고 
    # html 작성후 다시 셀렉터 값 복사

    for name in user:
    	print(name.text)
    	name_list.append(name.text)

    print('\n')





name_uniq= [] # 이름 목록 중복제거

name_uniq = list(set(name_list))

# for name in name_uniq:
# 	print(name , name_list.count(name))





    # print(url.get('href'))


    # users.append(user.get('title'))

# dic= dict(zip(dayss,urll))


# print(dic)
# print(users)











# for n in notices:
# 	print('n:',n)
	# print(n.text)
	# print(n.text.strip())


##