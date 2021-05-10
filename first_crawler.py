from bs4 import BeautifulSoup
from urllib.request import urlopen

URL1 = 'http://www.index.go.kr/unify/idx-info.do?idxCd=8005'
URL2 = 'http://www.index.go.kr/unify/idx-info.do?idxCd=8086'
URL3 = 'http://www.index.go.kr/unify/idx-info.do?idxCd=8086'

html1 = urlopen(URL1)
soup1 = BeautifulSoup(html1, 'lxml')
contents1 = soup1.find_all('tr', {'data-id':'tr_505601_1'})

html2 = urlopen(URL2)
soup2 = BeautifulSoup(html2, 'lxml')
contents2 = soup2.find_all('tr', {'data-id':'tr_422101_1'})

html3 = urlopen(URL3)
soup3 = BeautifulSoup(html3, 'lxml')
contents3 = soup3.find_all('tr', {'data-id':'tr_422101_3'})

text1 = ''
text2 = ''
text3 = ''

for item in contents1:
    text1 = text1 + item.get_text()
print(text1)

for item in contents2:
    text2 = text2 + item.get_text()
print(text2)

for item in contents3:
    text3 = text3 + item.get_text()
print(text3)