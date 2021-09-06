from selenium import webdriver
import time
 
# 크롬 웹브라우저 실행
path = "/Users/joyoonsik/Downloads/chromedriver"

 
driver = webdriver.Chrome(path)
url_list = []
content_list = ""
text = "검색하고 싶은 검색어 입력"
 
for i in range(1, 3):  # 1~2페이지까지의 블로그 내용을 읽어옴
    url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo='+ str(i) + '&rangeType=ALL&orderBy=sim&keyword=' + text
    driver.get(url)
    time.sleep(0.5)
 
    for j in range(1, 3): # 각 블로그 주소 저장
        titles = driver.find_element_by_xpath('/html/body/ui-view/div/main/div/div/section/div[2]/div['+str(j)+']/div/div[1]/div[1]/a[1]')
        title = titles.get_attribute('href')
        url_list.append(title)
 
print("url 수집 끝, 해당 url 데이터 크롤링")
 
for url in url_list: # 수집한 url 만큼 반복
    driver.get(url) # 해당 url로 이동
 
    driver.switch_to.frame('mainFrame')
    overlays = ".se-component.se-text.se-l-default" # 내용 크롤링
    # overlays = ".u_cbox.u_cbox_name.u_cbox_nick_area"
    
    contents = driver.find_elements_by_css_selector(overlays)
    
 
    for content in contents:
        content_list = content_list + content.text # content_list 라는 값에 + 하면서 점점 누적

print(content_list)
print('끝')
# driver.quit()
