import numpy as np

a = np.array([[1,2],[3,4]])
# 0轴表示横着看，所以是[1,2]，[3,4]两个向量
sum0 = np.sum(a, axis=0)
# 1轴表示竖着看，所以是[1,3]，[2,4]两个向量
sum1 = np.sum(a, axis=1)

print(sum0) # [4,6]
print(sum1) # [3,7]