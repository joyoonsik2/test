from selenium import webdriver

path = "/Users/joyoonsik/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get('https://blog.naver.com/a_shizuru/222386313286')

# 클래스가 tit_view인 h3태그
title = driver.find_elements_by_css_selector("p.se-text-paragraph")
print (title)
driver.quit()