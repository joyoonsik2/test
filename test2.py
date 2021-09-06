from selenium import webdriver
path = "/Users/joyoonsik/Downloads/chromedriver"
browser=webdriver.Chrome(path)
browser.get('https://blog.naver.com/macdaejjang/222484636943')

print(browser.find_element_by_class_name('u_cbox_text_wrap').text)