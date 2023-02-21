import re

# replace
tel_num = '010-10101010'
tel_num = re.subn('[^\d]', '', tel_num)[0]
print(tel_num)

# split
tel = '18248384538|13124093284|13124093248,13124093248'
print(re.split(r'(?:\||,)', tel))


# match
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")


# search
print(re.search('com', 'www.runoob.com'))
print(re.search('com', 'www.runoob.com').span())  

line = "Cats are smarter than dogs";
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")

# sub，替换
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

# findall
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)

# finditer
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print(match.group())

# 查找子字符串所有index
line = "00100100";
sub_line = '00100'
r = [m.start() for m in re.finditer(f'(?={sub_line})', line)]
print(r)