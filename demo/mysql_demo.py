import pymysql.cursors
import datetime

HOST='w03.test.yulore.com'
PORT=3306
USER='bigdata'
PASSWD='bigdb@2015qwe'

def get_conn():
    return pymysql.connect(host=HOST, port=PORT,user=USER,passwd=PASSWD,db='log_stat',charset='UTF8')
    
def get_count(log_date):
    conn = get_conn()
    cur = conn.cursor()
    sql = 'SELECT COUNT(0) FROM api_user_count_day WHERE date_time = %s'
    log_date_str = log_date.strftime('%Y-%m-%d')
    cur.execute(sql, (log_date_str))
    # 如果是更新或者插入的话需要执行commit
    # conn.commit()
    cur.close()
    conn.close()
    # return cur.fetchall()
    return cur.fetchone()[0]

if __name__ == '__main__':
	log_date = datetime.datetime.strptime('2017-05-21','%Y-%m-%d')
	print(get_count(log_date))