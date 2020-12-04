import xlwt
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import jsonpath
import json

k = 0
k0 = 0
i = 0
j = 0
file_name = r'/tmp/rongzi1.xls'  # 这是你要保存文件的文件路径和文件名
workbook = xlwt.Workbook()  # 表示新建xls工作簿
sheet1 = workbook.add_sheet('wangdai')  # 新建xls表，表的名字是worksheet

for num in range(1,14):
    url_ = 'https://www.p2peye.com/platform/rongzi/p'
    url = url_+str(num)
    session = HTMLSession()
    r = session.get(url)
    r.html.render()  # 动态渲染页面
    # print(r.html.html)
    r.html.encoding = 'utf-8'
    content = r.html.html
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # divs = soup.find_all('div', class_='wenzhang-content ng-binding iswhite-space')
    divs_0 = soup.find('table', class_='ui-table')
    divs = divs_0.find_all('tr')
    print(divs)

    i=0

    for div in divs:
        k0 = k0 + 1
        try:
            joke0 = div.find_all('td')[0].get_text()
            joke1 = div.find_all('td')[1].find('a').get_text()
            joke2 = div.find_all('td')[2].get_text()
            joke3 = div.find_all('td')[3].get_text()
            joke4 = div.find_all('td')[4].get_text()
            joke5 = div.find_all('td')[5].get_text()
            joke6 = div.find_all('td')[6].find_all('a')[0].get('href')
            joke6 = 'https:'+joke6

            # 把数据写入xls中，行，列，值
            sheet1.write(i + k, j, joke0)
            j = j + 1
            sheet1.write(i + k, j, joke1)
            j = j + 1
            sheet1.write(i + k, j, joke2)
            j = j + 1
            sheet1.write(i + k, j, joke3)
            j = j + 1
            sheet1.write(i + k, j, joke4)
            j = j + 1
            sheet1.write(i + k, j, joke5)
            j = j + 1
            sheet1.write(i + k, j, joke6)
            j = 0
            i = i + 1

            # print(joke0 + joke1 + joke2 + joke3 + joke4 + joke5 + "https:"+joke6 )
        except:
            print('ok-------------ok------------ok----------ok')
    k0=k0-1
    k = k0
workbook.save(file_name)


