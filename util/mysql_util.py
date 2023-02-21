from dbutils.pooled_db import PooledDB
import pymysql
import json

def get_conn(host, port, user, passwd, db):
    pool = PooledDB(pymysql,20,host=host,port=port,user=user,passwd=passwd,db=db,charset='utf8')
    return pool.connection() 

def get_dict_conn(host, port, user, passwd, db):
    pool = PooledDB(pymysql,20,host=host,port=port,user=user,passwd=passwd,db=db,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    return pool.connection()

def query_one(conn, sql):
    cur = conn.cursor()
    cur.execute(sql, ())
    cur.close()
    conn.close()
    return cur.fetchone()

def query_records(conn, sql):
    cur = conn.cursor()
    cur.execute(sql, ())
    cur.close()
    conn.close()
    return cur.fetchall()

if __name__=='__main__':
    dp_data_conn = get_dict_conn('mysql.dcloud.dianhua.cn', 3306, 'bigdata', 'bigdb@2015qwe', 'dp_data')
    sql = 'select * from dps_namekeyword_tel_blacklist where status=1 and country_code=86'
    results = query_records(dp_data_conn, sql)
    with open('C:\\Users\\Li Yujie\\Desktop\\namekeyword_tel_blaclist.json', 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result, separators=(',', ':'), ensure_ascii=False)+'\n')