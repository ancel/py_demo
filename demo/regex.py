import re

tel_num = '010-10101010'
tel_num = re.subn('[^\d]', '', tel_num)[0]
print(tel_num)