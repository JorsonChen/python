from datetime import datetime,timedelta

#获取当前时间
# now = datetime.now()
# print(now)
# print(type(now))

#获取指定日期和时间
# dt = datetime(2016, 1, 19, 21, 36, 23 )
# print(dt)

#时间转换为时间戳(小数点表示毫秒)
# dt = datetime(2016, 1, 19, 21, 36, 23 )
# print(dt.timestamp())

#时间戳转换为时间
# t = 1453210583.0
# print(datetime.fromtimestamp(t))

#字符串转换为时间
# strtotime = datetime.strptime('2016-1-16 21:47:52','%Y-%m-%d %H:%M:%S')
# print(strtotime)

#时间转换为字符串(星期，年月日，时分秒)
# now = datetime.now()
# print(now.strftime('%a,%Y %b %d, %H:%M:%S'))

#时间加减（须导入timedelta类,days:天数；hours：小时数；minutes：分钟数）
time = datetime(2016,1,16,22,2,34,123)
print(time)
deltime = time + timedelta(hours=1)
print(deltime)
addtime = time - timedelta(days=1,hours=3,minutes=1)
print(addtime)

