import datetime
import calendar
import time


# 获取月第一天
def getFirstDayOfMonth(d=datetime.date.today()):
    year = d.year
    month = d.month
    return datetime.date(year, month, 1)

# 获取月最后一天
def getLastDayOfMonth(d=datetime.date.today()):
    year = d.year
    month = d.month
    days = calendar.monthrange(year, month)[1]   
    return datetime.date(year,month,1)+datetime.timedelta(days=days-1)

# 获取上个月第一天
def getFirstDayOfLastMonth(d=datetime.date.today()):
    year = d.year
    month = d.month
    if month == 1 :
        month = 12
        year -= 1
    else :
        month -= 1
    return datetime.date(year, month, 1)

# 获取上个月最后一天
def getLastDayOfLastMonth(d=datetime.date.today()):
    year = d.year
    month = d.month
    if month == 1 :
        month = 12
        year -= 1
    else :
        month -= 1
    days = calendar.monthrange(year, month)[1]   
    return datetime.date(year,month,1)+datetime.timedelta(days=days-1)

def getCurrentTimeMillis():
    t = time.time()
    print (int(round(t * 1000)))

if __name__ == '__main__':
    print(getFirstDayOfLastMonth().strftime('%Y-%m-%d %X'))
    print(getLastDayOfLastMonth().strftime('%Y-%m-%d %X'))
    print(getLastDayOfLastMonth(datetime.date(2016,2,4)).strftime('%Y-%m-%d %X'))
    print(getFirstDayOfMonth().strftime('%Y-%m-%d %X'))
    print(getLastDayOfMonth().strftime('%Y-%m-%d %X'))
    print(datetime.datetime.today().strftime('%Y-%m-%d %X'))