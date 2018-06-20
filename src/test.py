# import time

# from src.currency import Currency

# client = InfluxDBClient(database='cr')
# client.write_points([{
#     'measurement':'dollar',
#     'tags':{'name':'abc'},
#     'fields':{'rate':'1313.1312112'}
# }])
#
# a = client.query("select time,bname,rate from prediction ;")  # WHERE bname ='工商银行' WHERE bname='兴业银行'
# for i in a['prediction']:
#     print(i)
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
#
# c = '100.1'
# print(c.isdecimal())
# l = [1, 2, 3]
# print(['a' for i in l])
count = 1  # 记录输出了几个数字
# for i in range(2, 1000):  # 搜索2~999之间的质数
#     f = False  # flag为是否被整除的标志位 初始化为false
#     for j in range(2, i):  # j为2~i-1之间的数 作为被除数
#         if i % j == 0:  # 如果i/j余0 即i被j整除
#             f = True  # 整除标志位置为True
#             break  # 因为已经找到一个除了1和本身的因数了 这个数肯定是合数 不用再循环下去直接退出循环
#     if not f:  # f为True是有除了本身的因数 not f就是没有找到其他因数 如果没找到的话：
#         print(i, end=' ')  # 输出i
#         if count % 10 == 0:  # 每输出10个数字打个回车 仅仅为了好看- -
#             print('')
#         count += 1  # 记录输出了几个数字

# for i in range(1800, 3000):  # 1000年~2999年
#     if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
#         # 先判断第一组条件 年数能被4整除且年数不能被100整除 是闰年
#         # 再判断第二组条件 年数能被400整除 是闰年
#         # 第一组第二组可以同时存在就是或的关系
#         print(i, end=' ')
#         if count % 5 == 0:
#             print('')
#         count += 1

a = {'Url': None, 'ErrorMsg': '', 'Data': {'Table': [
    {'CashBuyingPrice': 461.84, 'BuyingPrice': 477.17, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 479.09,
     'CurrId': 29, 'Id': 6044942, 'CurrName': '澳大利亚元(AUD)', 'SellPrice': 481.01},
    {'CashBuyingPrice': 460.24, 'BuyingPrice': 475.76, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 477.43,
     'CurrId': 18, 'Id': 6044944, 'CurrName': '新加坡元(SGD)', 'SellPrice': 479.1},
    {'CashBuyingPrice': 5.684, 'BuyingPrice': 5.865, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 5.885,
     'CurrId': 27, 'Id': 6044937, 'CurrName': '日元(JPY)', 'SellPrice': 5.906},
    {'CashBuyingPrice': 723.07, 'BuyingPrice': 747.45, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 750.07,
     'CurrId': 38, 'Id': 6044939, 'CurrName': '欧元(EUR)', 'SellPrice': 752.7},
    {'CashBuyingPrice': 77.24, 'BuyingPrice': 80.13, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 80.13,
     'CurrId': 81, 'Id': 6044933, 'CurrName': '澳门元(MOP)', 'SellPrice': 80.13},
    {'CashBuyingPrice': 641.42, 'BuyingPrice': 646.6, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 647.9,
     'CurrId': 14, 'Id': 6044929, 'CurrName': '美元(USD)', 'SellPrice': 649.2},
    {'CashBuyingPrice': 70.17, 'BuyingPrice': 72.5, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 72.8,
     'CurrId': 21, 'Id': 6044932, 'CurrName': '瑞典克朗(SEK)', 'SellPrice': 73.09},
    {'CashBuyingPrice': 0.563, 'BuyingPrice': 0.563, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 0.584,
     'CurrId': 88, 'Id': 6044934, 'CurrName': '韩国圆(KRW)', 'SellPrice': 0.605},
    {'CashBuyingPrice': 81.72, 'BuyingPrice': 82.38, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 82.55,
     'CurrId': 13, 'Id': 6044938, 'CurrName': '港元(HKD)', 'SellPrice': 82.71},
    {'CashBuyingPrice': 822.01, 'BuyingPrice': 849.72, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 852.71,
     'CurrId': 12, 'Id': 6044940, 'CurrName': '英镑(GBP)', 'SellPrice': 855.69},
    {'CashBuyingPrice': 19.07, 'BuyingPrice': 19.7, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 19.78,
     'CurrId': 84, 'Id': 6044935, 'CurrName': '泰铢(THB)', 'SellPrice': 19.86},
    {'CashBuyingPrice': 470.3, 'BuyingPrice': 485.91, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 487.86,
     'CurrId': 28, 'Id': 6044941, 'CurrName': '加拿大元(CAD)', 'SellPrice': 489.81},
    {'CashBuyingPrice': 627.71, 'BuyingPrice': 648.55, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 651.16,
     'CurrId': 15, 'Id': 6044943, 'CurrName': '瑞士法郎(CHF)', 'SellPrice': 653.76},
    {'CashBuyingPrice': 97.03, 'BuyingPrice': 100.25, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 100.65,
     'CurrId': 22, 'Id': 6044930, 'CurrName': '丹麦克朗(DKK)', 'SellPrice': 101.05},
    {'CashBuyingPrice': 76.29, 'BuyingPrice': 78.82, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 79.14,
     'CurrId': 23, 'Id': 6044931, 'CurrName': '挪威克朗(NOK)', 'SellPrice': 79.46},
    {'CashBuyingPrice': 72.92, 'BuyingPrice': 75.56, 'PublishTime': '2018-06-20T11:10:43', 'BenchMarkPrice': 75.56,
     'CurrId': 79, 'Id': 6044936, 'CurrName': '索莫尼(TJS)', 'SellPrice': 75.56}]}, 'ErrorCode': '0'}
reg = 'Data/Table'
index = '美元(USD)/SellPrice'
currency_list = a
r_l = reg.split('/')  # reg按/分隔

for i in r_l:
    currency_list = currency_list.get(i)  # 循环获取货币字典
for c in currency_list:  # 遍历每个货币种类
    if index.split('/')[0] in c.values():  # 查询的币种名称和汇率名以/分隔
        print(c.get('SellPrice'))
        print(type(c.get('SellPrice')))
        # c = a.get('Table').rstrip('0')
