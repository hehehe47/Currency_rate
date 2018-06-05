import time
import requests
import bs4
import json
import re

HEADERS = {
    '浦发银行': {
        'data': "metadata=CurrencyName%7CMdlPrc%7CBuyPrc%7CCashBuyPrc%7CSellPrc%7CCREATE_DATE&perpage=100&channelid=207567&searchword=",
        'header': {'Host': 'per.spdb.com.cn',
                   'Connection': 'keep-alive',
                   'Content-Length': '117',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Origin': 'http://per.spdb.com.cn',
                   'X-Requested-With': 'XMLHttpRequest',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Referer': 'http://per.spdb.com.cn/rate_query/201511/t20151119_23931.shtml',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                   'Cookie': 'Hm_lvt_e3386c9713baeb4f5230e617a0255dcb=1528080892; Hm_lpvt_e3386c9713baeb4f5230e617a0255dcb=1528080892; WASSESSION=IPLIuB1c5WA0aeL1Ff4AhNLsBuWrWcKNUEv_sdhhel0RRHQBpO6t!-474855487'
                   }
    },  # method:post return:json
    '兴业银行': {
        'data': '_search=false&dataSet.nd=' + str(time.time()).replace('.', '')[:13]
                + '&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc',
        'header': {
            'Host': 'personalbank.cib.com.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
            'Referer': 'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery.do',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': 'JSESSIONID=O1HNwrBWuWeT7hyrldMGBhasYm9NbrJpL_gXFji3rC7RZjmScWCO!194403045; '
                      'fp_ver=4.4.1; Hm_lvt_9311ae0af3818e9231e72458be9cdbce=1528081712,1528081860,1528082062; '
                      'BSFIT_EXPIRATION=1530749880033; BSFIT_OkLJUJ=FEGpc1NH9Z_nb3LNhoDsbzPYkZ5Uh1rf; '
                      'BSFIT_DEVICEID=zcckRoCa__HYnCeWB9ooHqSdMU1AkUoIEw2wlEdpCcRyWf_kLR_qUEzD0C11dVYuRmTGsTqPn5hu17plNxO89g21AANDW0uZC2QETAe3zDAO_oEaZKj5FKJaPkvmnxBhvGUP6UEAQUccBmYyG-ZsGdWIbN8ru3_7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22%24device_id%22%3A%22163c8c481ee58e-0e45e452b04c9e-3c3c5d0c-1049088-163c8c481ef470%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D'
        }
    },  # method:post return:json
    '浙商银行': {
        'data': 'dse_operationName=whpjInfoServiceSrvOp',
        'header': {
            'Host': 'perbank.czbank.com',
            'Connection': 'keep-alive',
            'Content-Length': '175',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://perbank.czbank.com',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://perbank.czbank.com/PERBANK/Trans',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': 'JSESSIONID=0000GhIcWuEfNe9cubbHuIGMDz8:1ajmhh9vj'
        }
    },  # method:post return:html
    '上海银行': {
        'data': 'validateRequest=dcbf61d68386e99c44cfea698b075833&go=bank_sellfund_pg_Banking&code=whpj',
        'header': {
            'Host': 'www.bosc.cn',
            'Connection': 'keep-alive',
            'Content-Length': '86',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://www.bosc.cn',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://www.bosc.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': 'JSESSIONID=4r3N2tr17bhp6ttuGsKCCsLlOAfEtOKzBmMrwB7fVXRAoP-u4yAT!-1764074769'
        }
    },  # method:post return:html

}

DOB = [
    {'name': '工商银行', 'type': 'h',
     'url': 'http://www.icbc.com.cn/ICBCDynamicSite/Optimize/Quotation/QuotationListIframe.aspx',
     'reg': 'td[class="tdCommonTableData"]', 'index': '3', 'header': False},  # 工商银行
    {'name': '农业银行', 'type': 'j', 'url': 'http://ewealth.abchina.com/app/data/api/DataService/ExchangeRateV2',
     'reg': 'Data/Table', 'index': '美元(USD)/SellPrice', 'header': False},  # 农业银行
    {'name': '中国银行', 'type': 'h', 'url': 'http://www.boc.cn/sourcedb/whpj/',
     'reg': 'td', 'index': '211', 'header': False},  # 中国银行
    {'name': '建设银行', 'type': 'x', 'url': 'http://forex1.ccb.com/cn/home/news/jshckpj_new.xml',
     'reg': '<OfrRateOfCash>(.*)</OfrRateOfCash>', 'index': '0', 'header': False},  # 建设银行
    {'name': '邮储银行', 'type': 'h', 'url': 'http://www.psbc.com/cms/queryExchange.do',
     'reg': 'td', 'index': '3', 'header': False},  # 邮储银行
    {'name': '交通银行', 'type': 'h',
     'url': 'http://www.bankcomm.com/BankCommSite/simple/cn/whpj/queryExchangeResult.do?type=simple',
     'reg': 'td', 'index': '121', 'header': False},  # 交通银行
    {'name': '招商银行', 'type': 'h', 'url': 'http://fx.cmbchina.com/Hq/',
     'reg': 'td[class="numberright"]', 'index': '12', 'header': False},  # 招商银行
    {'name': '浦发银行', 'type': 'j', 'url': 'http://per.spdb.com.cn/was5/web/search',
     'reg': 'rows', 'index': '美元 USD/SellPrc', 'header': True},  # 浦发银行  TODO need header get
    {'name': '兴业银行', 'type': 'j',
     'url': 'https://personalbank.cib.com.cn/pers/main/pubinfo/ifxQuotationQuery!list.do;jsessionid=O1HNwrBWuWeT7hyrldMGBhasYm9NbrJpL_gXFji3rC7RZjmScWCO!194403045?_search=false&dataSet.nd='
            + str(time.time()).replace('.', '')[:13] + '&dataSet.rows=80&dataSet.page=1&dataSet.sidx=&dataSet.sord=asc',
     'reg': 'rows', 'index': '3/cell', 'header': True},  # 兴业银行 TODO need header
    {'name': '华夏银行', 'type': 'h', 'url': 'https://sbank.hxb.com.cn/gateway/forexquote.jsp',
     'reg': 'td', 'index': '14', 'header': False},  # 华夏银行
    {'name': '广发银行', 'type': 'h', 'url': 'http://www.cgbchina.com.cn/searchExchangePrice.gsp?internal_time=14',
     'reg': 'td', 'index': '6', 'header': False},  # 广发银行
    {'name': '民生银行', 'type': 'h', 'url': 'http://www.kuaiyilicai.com/bank/rmbfx/b-cmbc.html',
     'reg': 'td', 'index': '13', 'header': False},  # 民生银行 网上没找到 快易理财网
    {'name': '中信银行', 'type': 'x',
     'url': 'https://etrade.citicbank.com/portalweb/cms/getForeignExchRate.htm?callback=jQuery111304100414144394351_1528092364386&_=1528092364387',
     'reg': '"curCode":"014001","totalPidPrice":"\d+\.\d+","totalSellPrice":"\d+\.\d+","cstexcBuyPrice":"\d+\.\d+","cstexcSellPrice":"(\d+\.\d+)"',
     'index': '0', 'header': False},  # 中信银行
    {'name': '光大银行', 'type': 'h', 'url': 'http://www.cebbank.com/eportal/ui?pageId=477257',
     'reg': 'td', 'index': '9', 'header': False},  # 光大银行
    {'name': '恒丰银行', 'type': 'h', 'url': 'http://www.hfbank.com.cn/ucms/hfyh/jsp/gryw/whpj.jsp',
     'reg': 'td', 'index': '25', 'header': False},  # 恒丰银行
    {'name': '浙商银行', 'type': 'h', 'url': 'https://perbank.czbank.com/PERBANK/WebBank',
     'reg': 'td', 'index': '18', 'header': True},  # 浙商银行 TODO need header and post
    {'name': '渤海银行', 'type': 'h', 'url': 'http://www.cbhb.com.cn/bhbank/admin/main?transName=exchange',
     'reg': 'td', 'index': '3', 'header': False},  # 渤海银行
    {'name': '平安银行', 'type': 'h', 'url': 'https://bank.pingan.com.cn/ibp/portal/exchange/qryExchangeList.do',
     'reg': 'td', 'index': '94', 'header': False},  # 平安银行
    {'name': '北京银行', 'type': 'h', 'url': 'http://www.kuaiyilicai.com/bank/rmbfx/b-bob.html',
     'reg': 'td', 'index': '13', 'header': False},  # 北京银行 网上没找到 快易理财网
    {'name': '上海银行', 'type': 'h', 'url': 'http://www.bosc.cn/WebServlet',
     'reg': 'td', 'index': '77', 'header': True},  # 上海银行 TODO need notify
    {'name': '江苏银行', 'type': 'j', 'url': 'http://www.jsbchina.cn/cms/FMoneyPriceQry.do',
     'reg': '', 'index': 'USDCNY/custOffer', 'header': False},  # 江苏银行
    {'name': '杭州银行', 'type': 'h', 'url': 'http://www.kuaiyilicai.com/bank/rmbfx/b-hzbank.html',
     'reg': 'td', 'index': '13', 'header': False},  # 杭州银行 网上没找到 快易理财网
    {'name': '南京银行', 'type': 'h', 'url': 'https://ebank.njcb.com.cn/perbank/PB00000016exchangeRateQry.do',
     'reg': 'td', 'index': '54', 'header': False},  # 南京银行
    {'name': '宁波银行', 'type': '', 'url': 'https://mybank.nbcb.com.cn/doorbank/cms_exchangeRate.do',
     'reg': '', 'index': '', 'header': True},  # 宁波银行 需要cookie的时间戳 就是header+get
    {'name': '花旗银行', 'type': 'h',
     'url': 'https://www.citibank.com.cn/CNGCB/aptc/rates/InitializeFXRate.do?locale=zh_CN',
     'reg': 'span', 'index': '58', 'header': False},  # 花旗银行
    {'name': '汇丰银行', 'type': 'h', 'url': 'http://www.hsbc.com.cn/1/2/misc-cn/exchange-rates/',
     'reg': 'td', 'index': '16', 'header': False},  # 汇丰银行
    {'name': '恒生银行', 'type': 'h', 'url': 'http://www.hangseng.com.cn/1/2/market-information-chi/deposit-exchange-rates',
     'reg': 'td[class="rateTbl2Row1"]', 'index': '14', 'header': False}  # 恒生银行
]



class Currency(object):
    def __init__(self, name, type, url, reg, index, header):
        self.name = name
        self.type = type
        self.url = url
        self.reg = reg
        self.index = index
        self.header = header

    def need_post(self):
        # TODO
        a = 1

    def add_header(self):
        # TODO
        a = 1
        a1 = 1
        a2= 1
        a3 = 1
        a4 = 1
        a5 = 1
        a6 = 1
        a7 = 1

    def get_usd(self):
        if self.header:
            r = requests.post(self.url, data=HEADERS[self.name]['data'], headers=HEADERS[self.name]['header'])
        else:
            r = requests.get(self.url)  # 获取页面信息
        if self.type == 'j':  # 若返回类型为json
            r = r.json()  # 先转换成json格式
            r_l = []
            if self.reg != '':
                r_l = self.reg.split('/')  # reg按/分隔
            currency_list = r
            try:
                for i in r_l:
                    currency_list = currency_list.get(i)  # 循环获取货币字典
                for c in currency_list:  # 遍历每个货币种类
                    if self.index.split('/')[0] in c.values():  # 查询的币种名称和汇率名以/分隔
                        if self.name == '兴业银行':
                            c = c.get(self.index.split('/')[1])[4].rstrip('0')
                        else:
                            c = c.get(self.index.split('/')[1]).rstrip('0')
                        if float(c) < 600:
                            c = str(float(c) * 100)
                        print(self.name + ':' + c)  # 去除尾部0
                        break
            except Exception as e:
                print(self.name + ' error: ')
                print(e)

        elif self.type == 'h':  # 返回正常页面
            try:
                b = bs4.BeautifulSoup(r.text, 'html.parser')
                c = b.select(self.reg)[int(self.index)].getText().replace(' ', '').replace('\n', '').replace('\r', '') \
                    .strip('0')
                if float(c) < 600:
                    c = str(float(c) * 100)
                print(self.name + ':' + c)
            except Exception as e:
                print(self.name + ' error: ')
                print(e)

        elif self.type == 'x':
            try:
                c = re.findall(self.reg, r.text)[int(self.index)]
                if float(c) < 600:
                    c = str(float(c) * 100)
                print(self.name + ':' + c)
            except Exception as e:
                print(self.name + ' error: ')
                print(e)


def sort_currency(list_of_currency):
    # TODO sort the currency
    return list_of_currency


for i in DOB:
    if i['type'] != '':  # and i==DOB[15]:
        c = Currency(i['name'], i['type'], i['url'], i['reg'], i['index'], i['header'])
        c.get_usd()
