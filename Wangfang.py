from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import jsonpath
import json

url = 'http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId=926509'
session = HTMLSession()
r = session.get(url)
r.html.render()  # 动态渲染页面
# print(r.html.html)
content = r.html.html
# print(content)
soup = BeautifulSoup(content, 'lxml')
# divs = soup.find_all('div', class_='wenzhang-content ng-binding iswhite-space')
divs_0 = soup.find('table', class_='MsoNormalTable')
divs = divs_0.find_all('tr')
# print(divs)
for div in divs:
    joke = div.find('p').find_all('span')
    jok_=''
    for joke_ in joke:
        jok_=jok_+joke_.get_text()
    joke0 = div.find_all('p')
    jok0_=''
    for joke1 in joke0:
        joke1_ = joke1.find_all('span')
        jok1_ = ''
        for joke1_ in joke1:
            try:
                # if(joke1_!=joke1.find('span',style="font-family:仿宋_GB2312;mso-hansi-font-family:黑体;mso-bidi-font-family:'Times New Roman';font-size:15.0000pt;mso-font-kerning:0.0000pt;")&&joke1_!=joke1.find('span',style="font-family:仿宋_GB2312;mso-hansi-font-family:黑体;mso-bidi-font-family:'Times New Roman';font-size:15.0000pt;mso-font-kerning:0.0000pt;")):
                jok1_ = jok1_ + joke1_.get_text()
            except:
                print(end="")
            jok0_=jok0_+jok1_


        #     joke1 = div.find('div', class_='Section0').find('div', align='center').find('table', class_='MsoNormalTable').find('tbody').find('tr', style='height:37.6000pt;').find('td',width='288').find('p').find_all('b')[0].find('span').get_text()
        #     joke2 = div.find('div', class_='Section0').find('div', align='center').find('table', class_='MsoNormalTable').find(
        #         'tbody').find('tr', style='height:37.6000pt;').find('td', width='470').find('p').find('span').get_text()
        #
        #     # joke = div.find('a', class_='contentHerf').find('div', class_='content').find('span').get_text()
        #     #  div.span.get_text()
    print(jok_ + "        " + jok0_)
    #     print(joke1  +"    "+  joke2)
print('-----------------------------')




