from influxdb import InfluxDBClient
import time

client = InfluxDBClient(database='cr')
# client.write_points([{
#     'measurement':'dollar',
#     'tags':{'name':'abc'},
#     'fields':{'rate':'1313.1312112'}
# }])

a = client.query("select rate from dollar ;")  # WHERE bname ='工商银行'
for i in a['dollar']:
    print(i['rate'])
    #
    # for j in i:
    #     print(j['bname'],j['rate'])
print(a['dollar'])

DOB = [
    {'name': '工商银行', 'type': 'h',
     'url': 'http://www.icbc.com.cn/ICBCDynamicSite/Optimize/Quotation/QuotationListIframe.aspx',
     'reg': 'td[class="tdCommonTableData"]', 'index': '3', 'header': False},  # 工商银行 0
    {'name': '农业银行', 'type': 'j', 'url': 'http://ewealth.abchina.com/app/data/api/DataService/ExchangeRateV2',
     'reg': 'Data/Table', 'index': '美元(USD)/SellPrice', 'header': False},  # 农业银行 1
    {'name': '中国银行', 'type': 'h', 'url': 'http://www.boc.cn/sourcedb/whpj/',
     'reg': 'td', 'index': '211', 'header': False},  # 中国银行 2
    {'name': '建设银行', 'type': 'x', 'url': 'http://forex1.ccb.com/cn/home/news/jshckpj_new.xml',
     'reg': '<OfrRateOfCash>(.*)</OfrRateOfCash>', 'index': '0', 'header': False},  # 建设银行 3
    {'name': '邮储银行', 'type': 'h', 'url': 'http://www.psbc.com/cms/queryExchange.do',
     'reg': 'td', 'index': '3', 'header': False},  # 邮储银行 4
    {'name': '交通银行', 'type': 'h',
     'url': 'http://www.bankcomm.com/BankCommSite/simple/cn/whpj/queryExchangeResult.do?type=simple',
     'reg': 'td', 'index': '121', 'header': False},  # 交通银行 5
    {'name': '招商银行', 'type': 'h', 'url': 'http://fx.cmbchina.com/Hq/',
     'reg': 'td[class="numberright"]', 'index': '12', 'header': False},  # 招商银行 6
    {'name': '浦发银行', 'type': 'j', 'url': 'http://per.spdb.com.cn/was5/web/search',
     'reg': 'rows', 'index': '美元 USD/SellPrc', 'header': True},  # 浦发银行  TODO need header get
    {'name': '兴业银行', 'type': 'j',
     'url': 'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery!list.do;jsessionid=O1HNwrBWuWeT7hyrldMGBhasYm9NbrJpL_gXFji3rC7RZjmScWCO!194403045?_search=false&dataSet.nd='
            + str(time.time()).replace('.', '')[:13] + '&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc',
     'reg': 'rows', 'index': '3/cell', 'header': True},  # 兴业银行 TODO need header
    {'name': '华夏银行', 'type': 'h', 'url': 'https://sbank.hxb.com.cn/gateway/forexquote.jsp',
     'reg': 'td', 'index': '14', 'header': False},  # 华夏银行 9
    {'name': '广发银行', 'type': 'h', 'url': 'http://www.cgbchina.com.cn/searchExchangePrice.gsp?internal_time=14',
     'reg': 'td', 'index': '6', 'header': False},  # 广发银行 10
    {'name': '民生银行', 'type': 'h', 'url': 'http://www.kuaiyilicai.com/bank/rmbfx/b-cmbc.html',
     'reg': 'td', 'index': '13', 'header': False},  # 民生银行 网上没找到 快易理财网
    {'name': '中信银行', 'type': 'x',
     'url': 'https://etrade.citicbank.com/portalweb/cms/getForeignExchRate.htm?callback=jQuery111304100414144394351_1528092364386&_=1528092364387',
     'reg': '"curCode":"014001","totalPidPrice":"\d+\.\d+","totalSellPrice":"\d+\.\d+","cstexcBuyPrice":"\d+\.\d+","cstexcSellPrice":"(\d+\.\d+)"',
     'index': '0', 'header': False},  # 中信银行 11
    {'name': '光大银行', 'type': 'h', 'url': 'http://www.cebbank.com/eportal/ui?pageId=477257',
     'reg': 'td', 'index': '9', 'header': False},  # 光大银行 12
    {'name': '恒丰银行', 'type': 'h', 'url': 'http://www.hfbank.com.cn/ucms/hfyh/jsp/gryw/whpj.jsp',
     'reg': 'td', 'index': '25', 'header': False},  # 恒丰银行 13
    {'name': '浙商银行', 'type': 'h', 'url': 'https://perbank.czbank.com/PERBANK/WebBank',
     'reg': 'td', 'index': '18', 'header': True},  # 浙商银行 TODO need header and post
    {'name': '渤海银行', 'type': 'h', 'url': 'http://www.cbhb.com.cn/bhbank/admin/main?transName=exchange',
     'reg': 'td', 'index': '3', 'header': False},  # 渤海银行 15
    {'name': '平安银行', 'type': 'h', 'url': 'https://bank.pingan.com.cn/ibp/portal/exchange/qryExchangeList.do',
     'reg': 'td', 'index': '94', 'header': False},  # 平安银行 16
    {'name': '北京银行', 'type': 'h', 'url': 'http://www.kuaiyilicai.com/bank/rmbfx/b-bob.html',
     'reg': 'td', 'index': '13', 'header': False},  # 北京银行 网上没找到 快易理财网
    {'name': '上海银行', 'type': 'h', 'url': 'http://www.bosc.cn/WebServlet',
     'reg': 'td', 'index': '77', 'header': True},  # 上海银行 TODO need notify
    {'name': '江苏银行', 'type': 'j', 'url': 'http://www.jsbchina.cn/cms/FMoneyPriceQry.do',
     'reg': '', 'index': 'USDCNY/custOffer', 'header': False},  # 江苏银行 19
    {'name': '杭州银行', 'type': 'h', 'url': 'http://www.kuaiyilicai.com/bank/rmbfx/b-hzbank.html',
     'reg': 'td', 'index': '13', 'header': False},  # 杭州银行 网上没找到 快易理财网
    {'name': '南京银行', 'type': 'h', 'url': 'https://ebank.njcb.com.cn/perbank/PB00000016exchangeRateQry.do',
     'reg': 'td', 'index': '54', 'header': False},  # 南京银行 21
    {'name': '宁波银行', 'type': '', 'url': 'https://mybank.nbcb.com.cn/doorbank/cms_exchangeRate.do',
     'reg': '', 'index': '', 'header': True},  # 宁波银行 需要cookie的时间戳 就是header+get
    {'name': '花旗银行', 'type': 'h',
     'url': 'https://www.citibank.com.cn/CNGCB/aptc/rates/InitializeFXRate.do?locale=zh_CN',
     'reg': 'span', 'index': '58', 'header': False},  # 花旗银行 23
    {'name': '汇丰银行', 'type': 'h', 'url': 'http://www.hsbc.com.cn/1/2/misc-cn/exchange-rates/',
     'reg': 'td', 'index': '16', 'header': False},  # 汇丰银行 24
    {'name': '恒生银行', 'type': 'h', 'url': 'http://www.hangseng.com.cn/1/2/market-information-chi/deposit-exchange-rates',
     'reg': 'td[class="rateTbl2Row1"]', 'index': '14', 'header': False}  # 恒生银行 25
]

# import requests
# import bs4
# r = requests.get('http://www.jsbchina.cn/cms/FMoneyPriceQry.do')
# print(r.text)
# b = bs4.BeautifulSoup(r.text,'html.parser')
# print()
# ind = b.select('td').index(b.select('td')[0])
# print(ind)
# for i,j in enumerate(b.select('td')):
#     print(i,j)
# print(b)
# print(a)
