from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('172.18.19.121',27017)
    db = client['data-china']
    coll = db['china-dianping-life-170327']
    # coll = db['china-0579kk-life-touzidanbao-170221']
    result = coll.find({},{"category":1,"_id":0})
    for x in result:
        print(x['category'][0])
        