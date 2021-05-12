from bs4 import BeautifulSoup
from urllib.request import urlopen
import matplotlib.pyplot as plt

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

y1=[]
y2=[]
y3=[]
x=[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

y1.extend([1860, 1830, 1840, 1820, 1750, 1760, 1730, 1670, 1630])
y2.extend([2832, 2900, 2998, 3083, 3260, 3391, 3493, 3531, 3528])
y3.extend([2799, 2899, 2995, 3095, 3260, 3411, 3589, 3693, 3744])

plt.plot(x, y1, color='b')
plt.plot(x, y2, color = 'g')
plt.plot(x, y3, color = 'r')
plt.suptitle('상대적 빈곤율 및 1인당 국민총소득')
plt.show()