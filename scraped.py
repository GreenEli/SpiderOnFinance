import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

base_url = 'https://www.qiushibaike.com/text/page/'  # 设定一个网址不变的部分，然后我们只要每次在这个后面加数字就可以了
for num in range(1, 5): # 设置循环，让num分别等于1-10
    print('第{}页'.format(num))
    r = requests.get(base_url + str(num), headers = headers) #这里对网址进行一个修改
    r.encoding='uttf-8'
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    divs = soup.find_all('div', class_ = 'article block untagged mb15 typs_hot')
    for div in divs:
        joke = div.find('a', class_='contentHerf').find('div',class_='content').find('span').get_text()
      #  div.span.get_text()
        print(joke)
        print('-------')