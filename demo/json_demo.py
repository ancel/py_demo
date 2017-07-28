import json

over_flag = dict()
over_flag['shopid'] = 'test'
print(json.dumps(over_flag, separators=(',',':'), ensure_ascii=False))