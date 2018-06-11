from influxdb import InfluxDBClient
# import time

# from src.currency import Currency

client = InfluxDBClient(database='cr')
# client.write_points([{
#     'measurement':'dollar',
#     'tags':{'name':'abc'},
#     'fields':{'rate':'1313.1312112'}
# }])
#
a = client.query("select time,rate from dollar WHERE bname='兴业银行';")  # WHERE bname ='工商银行'
for i in a['dollar']:
    print(i)
#     #
#     # for j in i:
#     #     print(j['bname'],j['rate'])
# print(a['dollar'])



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
# r = requests.get('http://www.shengjingbank.com.cn/gjyw/flbz/whzjywsfb/wbpjb/index.shtml')
# r = requests.post(DOB[8]['url'], headers=HEADERS['兴业银行']['header'], data=HEADERS['兴业银行']['data'])
# s = r.headers['Set-Cookie'].split(',')[1].strip(' ').split(';')[0]
# a = {
#     'Cookie': 'JSESSIONID=JIbUKarK8UfDwmyRYsMY4I35Y_3w39E30fD3IVKMK5RDMw1tQ6k_!-1924768203;'
#               'fp_ver=4.4.1; Hm_lvt_9311ae0af3818e9231e72458be9cdbce=1528081712,1528081860,1528082062;'
#               'BSFIT_EXPIRATION=1530749880033; BSFIT_OkLJUJ=FEGpc1NH9Z_nb3LNhoDsbzPYkZ5Uh1rf;'
#               'BSFIT_DEVICEID=zcckRoCa__HYnCeWB9ooHqSdMU1AkUoIEw2wlEdpCcRyWf_kLR_qUEzD0C11dVYuRmTGsTqPn5hu17plNx'
#               'O89g21AANDW0uZC2QETAe3zDAO_oEaZKj5FKJaPkvmnxBhvGUP6UEAQUccBmYyG-ZsGdWIbN8ru3_7; sensorsdata2015js'
#               'sdkcross=%7B%22distinct_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%'
#               '22%2C%22%24device_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%'
#               '22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
# }
# print(a['Cookie'].replace('JSESSIONID=JIbUKarK8UfDwmyRYsMY4I35Y_3w39E30fD3IVKMK5RDMw1tQ6k_!-1924768203;',s))
# print()
# b = bs4.BeautifulSoup(r.text,'html.parser')
# print()
# ind = b.select('td[class="rateTbl2Row1"]')
# print(ind[14])
# for i,j in enumerate(b.select('td')):
#     print(i,j)
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
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1528337632.329)))
# LOG_FILE = '..\\log\\currency_rate.xlsx'

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

# l = [{'name': 'gg', 'rate': '1'}, {'name': 'aa', 'rate': '2'}, {'name': 'bb', 'rate': '3'},
#      {'name': 'cc', 'rate': 'a'}]
# print([k['rate'] for k in l])
# print('Get all' if '??' not in [k['rate'] for k in l] else 'Sth missing')
# print(['Get all', 'Sth missing']['??' in [k['rate'] for k in l]])
# s = '643'
# name = 'a'
# print(name+":%.2f" %(float(s)))
# import numpy as np
#
# print(type(np.linspace(-np.pi, np.pi, 100)))
# print(type(np.cos(np.linspace(-np.pi, np.pi, 100))))
# l = [1,2,3,4,5]
# for i in range(len(l)):
#     print(l[i])

c = '100.1'
print(c.isdecimal())