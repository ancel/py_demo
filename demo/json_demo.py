import json

over_flag = dict()
over_flag['shopid'] = 'test'
print(json.dumps(over_flag, separators=(',',':'), ensure_ascii=False))

class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 

print(json.dumps(over_flag, separators=(',',':'), ensure_ascii=False, cls=DateEncoder))
# 对象转json
print(json.dumps(x, separators=(',',':'), default=lambda obj: obj.__dict__, ensure_ascii=False))