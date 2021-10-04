"""
# File: test.py
# Written by JessyTsui
# Time: 2021/10/3 11:40 下午
# IDE: PyCharm
# Have a good day！
"""

import xlwt  # .py文件要在和xlwt和xlrd同一层目录，不然报错

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('Sheet1')  # sheet页第一页

f = open('1.txt', encoding='utf-8')  # .py文件和TestCase.txt同一目录，第一个参数是路径

row_excel = 0  # 行

for line in f:
    line = line.strip('\n')  # 去掉换行符
    line = line.split('+')  # 每一行以"+"分隔

    print(line)  # 测试

    col_excel = 0  # 列
    len_line = len(line)
    for j in range(len_line):
        print(line[j])  # 测试
        ws.write(row_excel, col_excel, line[j])
        col_excel += 1
        wb.save('1.xls')  # 输出在同一目录

    row_excel += 1

f.close
