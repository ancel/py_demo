import tarfile

# 归档压缩
tf = tarfile.open('myprog.tar.gz', 'w:gz')
tf.add("MYPROG")
tf.close()

# 解压
tf = tarfile.open('myprog.tar.gz')
tf.extractall()
tf.close()

# 读取归档文件内容
tf = tarfile.open('myprog.tar.gz')
tf.list()
tf.read
print(tf.getmembers())
f = tf.getmember('MYPROG/hello.py')
print(f.name)
print(f.size)
print(f.tobuf())
f.isfile()
tf.close()