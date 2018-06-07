from influxdb import InfluxDBClient

LOB = ['工商银行', '农业银行', '中国银行', '建设银行', '邮储银行', '交通银行', '招商银行', '浦发银行', '兴业银行', '华夏银行', '广发银行', '民生银行', '中信银行', ' 光大银行',
       '恒丰银行', '浙商银行', '渤海银行', '平安银行', '北京银行', '上海银行', '江苏银行', '杭州银行', '南京银行', '宁波银行', '花旗银行', '汇丰银行', '恒生银行']

client = InfluxDBClient(database='cr')
# for i in LOB:
#     # print(i)
points = client.query("SELECT bname,rate FROM dollar;")['dollar']  # WHERE bname='"+i+"';") #全量取数据库数据
for p in points:  # points[{time:aa,bname:bb,rate:aa},{time:aa,bname:bb,rate:aa}]
    print(p['time'])
