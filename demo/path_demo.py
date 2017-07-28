import os

a = 'C:\\Users\\Li Yujie\\Desktop\\py_demo\\demo'
b = 'path_demo.py'
this_path = os.path.join(a,b)
print(this_path)
print(os.path.basename(a+'\\123'))
this_path = a+'\\123\\'
print(os.path.realpath(this_path))
print(os.path.relpath(this_path))
print(os.path.normpath(this_path))
print(os.path.abspath(this_path))
print(os.path.os.path.dirname(this_path))

