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
end_time = datetime.datetime.now()
    print('use time: {} (s)'.format(str((end_time-start_time).seconds)))