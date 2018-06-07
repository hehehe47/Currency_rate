from influxdb import InfluxDBClient
import time

# from src.currency import Currency

client = InfluxDBClient(database='cr')
# client.write_points([{
#     'measurement':'dollar',
#     'tags':{'name':'abc'},
#     'fields':{'rate':'1313.1312112'}
# }])

# a = client.query("select rate from dollar WHERE bname='工商银行';")  # WHERE bname ='工商银行'
# for i in a['dollar']:
#     print(i['rate'])
#     #
#     # for j in i:
#     #     print(j['bname'],j['rate'])
# print(a['dollar'])



import requests
import bs4

# header = {
# 'Host':'mybank.nbcb.com.cn',
# 'Connection':'keep-alive',
# 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
# 'Cookie':'Hm_lvt_8b9480950a6cadd80a66f238d3e4542e=1528097970,1528097991'
# }
# r = requests.post(DOB[8]['url'], headers=HEADERS['兴业银行']['header'], data=HEADERS['兴业银行']['data'])
# print(r.text)
# b = bs4.BeautifulSoup(r.text,'html.parser')
# print()
# ind = b.select('td').index(b.select('td')[0])
# print(ind)
# for i,j in enumerate(b.select('td')):
# print(i,j)
# print(b)
# print(a)
#
# import xlsxwriter
#
# worksheet = xlsxwriter.Workbook('1.xlsx')
# worksheet.close()
# rate =None
# print([rate,'??'][rate])
# i = DOB[8]
# c = Currency(i['name'], i['rt_type'], i['url'], i['reg'], i['index'], i['header'])
# c.get_usd()
# import time
# # print(time.strftime('%Y-%M-%D %H:%m:%s',time.localtime(1528097970)))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528337632.329)))
LOG_FILE = '..\\log\\currency_rate.xlsx'

# print(ord('A'))
# print(chr(97))

# while i<=26*26:
#     s = ''
#     num1 = int(i/26)
#     num2 = i%26
#     print(chr(64+num1)*[0,1][num1!=0]+chr(64+num2))
#     i+=1
# import openpyxl
# d = []
# for i in range(0, 26 * 26 * 27 - 1):
#     l = []
#     while i != 0:
#         l.append(i % 27)
#         i = int(i / 27)
#     l.reverse()
#     a = ''.join([chr(64 + i) for i in l])
#     if '@' not in a and a:
#         d.append(a)
#     i += 1
# #
# # for i, j in enumerate(d):
# #     print(i, j)
#
# workbook = openpyxl.Workbook('1.xlsx')
# sheet = workbook.get_sheet_names()
# print(sheet)
# for i in sheet:
#     print(i)
# for i, j in enumerate(d):
#     sheet[j+'1'] = j+'asdf'
#     break
# workbook.save('1.xlsx')