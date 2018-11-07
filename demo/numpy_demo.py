import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))


# 使用数组创建ndarray
a = np.array([2.0, 3, 4])
print(a)
b = np.array([(1.5,2,3), (4,5,6)])
print(b)
c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)

# 初始化矩阵，赋予默认值
print(np.zeros( (3,4) ))
print(np.ones( (2, 3, 4), dtype=np.int16 ))
print(np.empty( (2,3) )   )

# 10=<生成数<30, 步长为5
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ))

# 0-2等长分成个元素
print(np.linspace( 0, 2, 9 ))
from numpy import pi
print(np.linspace( 0, 2*pi, 100 ))