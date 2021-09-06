import requests 
from bs4 import BeautifulSoup 
import unicodedata # 서울시 뉴스 
url = 'https://mediahub.seoul.go.kr/archives/2000338' 
html = requests.get(url) 
html_text = html.text 
soup = BeautifulSoup(html_text, "lxml") 
title = soup.find("h3", class_="tit").get_text() 
print('title:' + title) 
content = soup.find("div", class_="reply-count").get_text() 
content = unicodedata.normalize("NFKD", content) 
print('content:' + content)
