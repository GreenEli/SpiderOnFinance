import requests
import jsonpath
import json
import xlwt


k=0
file_name = r'/tmp/test4.xls'  # 这是你要保存文件的文件路径和文件名
workbook = xlwt.Workbook()  # 表示新建xls工作簿
sheet1 = workbook.add_sheet('wangdai')  # 新建xls表，表的名字是worksheet
try:
    for num in range(198, 285):
        # 获取拉勾网城市json字符串
        num = num + 1
        url0 = 'https://www.p2peye.com/platformData.php?mod=issue&ajax=1&action=getPage&page='
        url = url0 + str(num)
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        response = requests.get(url, headers=headers)
        html_str = response.content.decode()

        # 把json格式字符串转换成python对象
        jsonobj = json.loads(html_str)

        # 从根节点开始，获取所有key为name的值
        # citylist0 = jsonpath.jsonpath(jsonobj, '$..name')
        # citylist1 = jsonpath.jsonpath(jsonobj, '$..city_name')
        # citylist2 = jsonpath.jsonpath(jsonobj, '$..black_type_name')
        # citylist3 = jsonpath.jsonpath(jsonobj, '$..black_url')
        # citylist4 = jsonpath.jsonpath(jsonobj, '$..online_time')
        # citylist5 = jsonpath.jsonpath(jsonobj, '$..black_time')

        citylist0 = jsonpath.jsonpath(jsonobj, '$..black_time')
        citylist1 = jsonpath.jsonpath(jsonobj, '$..name')
        citylist2 = jsonpath.jsonpath(jsonobj, '$..city_name')
        citylist3 = jsonpath.jsonpath(jsonobj, '$..online_time')
        citylist4 = jsonpath.jsonpath(jsonobj, '$..black_type_name')
        citylist5 = jsonpath.jsonpath(jsonobj, '$..black_url')
        print(citylist0)
        print(citylist1)
        print(citylist2)
        print(citylist3)
        print(citylist4)
        print(citylist5)
        i = 0
        j = 0
        for citylist in citylist0:
            # 把数据写入xls中，行，列，值
            sheet1.write(i + k, j, str(citylist0[i]))
            j = j + 1
            sheet1.write(i + k, j, str(citylist1[i]))
            j = j + 1
            sheet1.write(i + k, j, str(citylist2[i]))
            j = j + 1
            sheet1.write(i + k, j, str(citylist3[i]))
            j = j + 1
            sheet1.write(i + k, j, str(citylist4[i]))
            j = j + 1
            sheet1.write(i + k, j, str(citylist5[i]))
            j = 0
            i = i + 1
        k = k + 20
    workbook.save(file_name)

    # 保存xls到file_name的路径下和文件名
    # i=0
    # while(citylist[i]!=None):
    #     print(citylist[i])
    #     url = 'http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId='
    #     headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
    #     response = requests.get(url+str(citylist[i]), headers=headers)
    #     response.encoding='utf-8'
    #     print(response.text)
    #     i=i+1

    # # 写入文件
    # with open('city_name.txt', 'w') as f:
    #     content = json.dumps(citylist, ensure_ascii=False)
    #     f.write(content)
    #     print(content)
except:
    print('ok')
