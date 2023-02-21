import datetime
import time

def utc2local(utc_st):
    # UTC时间转本地时间（+8:00）
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st

def local2utc(local_st):
    # 本地时间转UTC时间（-8:00）
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st
UTC_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
LOCAL_FORMAT = '%Y-%m-%d %H:%M:%S'

d = '2017-05-21T19:00:00.000Z'
print(utc2local(datetime.datetime.strptime(d, UTC_FORMAT)).strftime('%Y-%m-%d %H:%M:%S'))
utc_time = datetime.datetime(2014, 9, 18, 10, 42, 16, 126000)
print(utc2local(utc_time).strftime('%Y-%m-%d %H:%M:%S'))

start_time = datetime.datetime.now()
# {实际代码}
print(start_time)
end_time = datetime.datetime.now()
print('use time: {} (s)'.format(str((end_time-start_time).seconds)))

d = '2017-05-21 19:00:00'
start = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
d = '2017-05-21 14:00:00'
end = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
print(start<end)

import datetime
 
# 获取今天（现在时间）
today = datetime.datetime.today()
# 昨天
yesterday = today - datetime.timedelta(days=1)
# 明天
tomorrow = today + datetime.timedelta(days=1)
 
# 获取当前日期
date = datetime.date.today()
# 获取一秒后的时间
s = today + datetime.timedelta(seconds=1)
# 获取一分钟后的时间
m = today + datetime.timedelta(minutes=1)
# 获取一小时后的时间
h = today + datetime.timedelta(hours=1)
# 获取一年后的时间
y = today + datetime.timedelta(days=365)
 
print('获取今天（现在时间）：{}\n'.format(today),
      '昨天：{}\n'.format(yesterday),
      '明天：{}\n'.format(tomorrow),
      '获取当前日期：{}\n'.format(date.strftime('%Y%m%d')),
      '一秒后的时间：{}\n'.format(s),
      '一分钟后的时间：{}\n'.format(m),
      '一小时后的时间：{}\n'.format(h),
      '一年后的时间：{}'.format(y))

# 时间戳转日期
import datetime
timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)