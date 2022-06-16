import numpy as np
import scipy.sparse as ss
import random
# 随机产生行、列坐标和值
a = random.sample(range(0, 9), 5)
b = random.sample(range(0, 9), 5)
c = random.sample(range(1, 100), 5)
# 将list数据转为array数组
rows = np.array(a)
print(rows,"#rows")
cols = np.array(b)
print(cols, "#cols")
v = np.array(c)
print(v,"#values")
# coo_matrix函数生成稀疏矩阵
sparseM = ss.coo_matrix((v,(rows,cols)))
print(sparseM, "#sparseM,", "shape is ", sparseM.shape)
# todense将稀疏矩阵转为完全阵
fullM = sparseM.todense()
print(fullM, "#fullM,", "shape is ", fullM.shape)


a = np.zeros((3, 4))
a[1, 2] = 12
a[2, 2] = 22
print(a)
print(ss.csc_matrix(a))
print(ss.csc_matrix(a).todense())