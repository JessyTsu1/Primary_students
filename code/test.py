"""
# File: test.py
# Written by JessyTsui
# Time: 2021/10/3 11:41 下午
# IDE: PyCharm
# Have a good day！
"""

import requests, xlwt, sys
from lxml import etree
import lxml

for i in range(1,20):
    url = "https://school.wjszx.com.cn/senior/introduce-{}.html".format(i)

    html = requests.get(url)
    html.encoding = "utf-8"
    selecter = etree.HTML(html.text)
    # xpath里可能有双引号，所以我们加上三引号比较靠谱
    name = selecter.xpath("""//h1/text()""")
    # print(name)
    time = selecter.xpath("""/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/text()""")
    print(time)
    test = selecter.xpath("""/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[position()<4]/text()""")

    print(name)
    print(test)
    print('')
    # print(test)



def getList(url):
    html = requests.get(url)
    html.encoding = "utf-8"
    selecter = etree.HTML(html.text)
    # 将你的xpath复制到三引号里面，因为xpath里可能有双引号，所以我们加上三引号比较靠谱
    name = selecter.xpath("""//h1/text()""")
    # print(name)
    test = selecter.xpath("""/html/body/div[3]/div[2]/div/div[2]/div[1]/div[3]/ul/li[position()<4]/text()""")
    # print(test)

    info = []

    # print(name.text.strip()+"\t"+test.strip()+"\t")
    # # 将结果放入列表
    # info.append([name.text.strip().decode("utf-8"), test.strip().decode("utf-8")])
    # print(info)
    return name, test


# 创建excel 表
def createExcelAndSheet(excelName, sheetName, *colName):
    # 创建excel工作簿
    exce = xlwt.Workbook()
    # 创建sheet
    sheet = exce.add_sheet(sheetName, cell_overwrite_ok=True)
    # 在第一行设置表头
    for index, val in enumerate(colName):
        sheet.write(0, index, val)
    # 插入数据
    row_num = 1
    page_num = 1
    while True:
        print("page" + str(page_num))
        url = "https://school.wjszx.com.cn/senior/introduce-{}.html".format(i)
        # page_num = page_num + 1
        info = getList(url)
        # 如果列表长度大于0，则表示有内容，否则页面为空跳出循环
        if (len(info) > 0):
            for i, line in enumerate(info):
                sheet.write(row_num, 0, row_num)
                for j, element in enumerate(line):
                    sheet.write(row_num, j + 1, element)
                    # print(str(row_num)+"\t"+str(j)+element)
                row_num = row_num + 1
        else:
            break
    exce.save(excelName)


# if __name__ == "__main__":
#     createExcelAndSheet("students.xls", "stu", "name", "test")

