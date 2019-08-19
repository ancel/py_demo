import os
import subprocess
import threading


LOCK = threading.RLock()

def get_files(path, file_filter=None): 
    ret = [] 
    if os.path.isfile(path):
        if None==file_filter or file_filter(path):
            ret.append(path)
    else:
        for root, dirs, files in os.walk(path): 
            for f in files: 
                filename = os.path.join(root,f)
                if None==file_filter or file_filter(filename):
                    ret.append(filename)
    return ret  

def get_dirs(path): 
    assert os.path.isdir(path), '%s not exist.' % path 
    ret = [] 
    for root, dirs, files in os.walk(path): 
        for d in dirs: 
            ret.append(os.path.join(root,d)) 
    return ret 

def ensure_dir(file_path):
    with LOCK:
        directory = os.path.dirname(file_path)
        if ''!=directory and not os.path.exists(directory):
            os.makedirs(directory)

def get_relative_path(parent_path, child_path):
    parent_path = os.path.abspath(parent_path)
    child_path = os.path.abspath(child_path)
    if not child_path.startswith(parent_path):
        raise Exception('path can not be relative')
    relative_path = child_path[len(parent_path):]
    if relative_path.startswith('/'):
        relative_path = relative_path[1:]
    return relative_path

# 通过tail获取最后行
def get_tail_lines(file_path, line_count):
    res = subprocess.Popen('tail -{} {}'.format(str(line_count),file_path),
    shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True) 
    result = res.stdout.readlines() 
    result2 = []
    for x in result:
        result2.append(x.decode())
    return result2

def get_last_line(file_path): 
    with open(file_path, mode='rb') as f:
        pos = 0
        f.seek(pos, 2)
        while True:  
            pos = pos - 1  
            try:  
                f.seek(pos,2)  #从文件末尾开始读 
                if f.read(1) == b'\n':
                    return f.readline().strip().decode()
            except BaseException as e:     #到达文件第一行，直接读取，退出  
                f.seek(0, 0)        
                return f.readline().strip().decode()

def get_last_not_blank_line(file_path): 
    with open(file_path, mode='rb') as f:
        pos = 0
        f.seek(pos, 2)
        while True:  
            pos = pos - 1  
            try:  
                f.seek(pos,2)  #从文件末尾开始读 
                if f.read(1) == b'\n':
                    line = f.readline().strip().decode()
                    if ''!=line:
                        return line
            except BaseException as e:     #到达文件第一行，直接读取，退出  
                f.seek(0, 0)        
                return f.readline().strip().decode()  

def get_line_count(file_path):
    count = 0
    with open(file_path, mode='rb') as f:
        line_sperator = bytes('\n', encoding="utf8")
        while True:  
            buf = f.read(1024 * 8192)  
            if not buf:  
                break  
            count += buf.count(line_sperator)  

    return count

# 比较两个文件，导出a和b的交集
def intersection(a, b):
    a_set = set()
    b_set = set()
    with open(a,mode='r') as f:
        for line in f.readlines():
            a_set.add(line.strip())
    with open(b) as f:
        for line in f.readlines():
            b_set.add(line.strip())
    return a_set & b_set

# 比较两个文件，导出b相对于a的差集
def difference(a, b):
    a_set = set()
    b_set = set()
    with open(a, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace('（','(').replace('）',')')
            a_set.add(line)
    with open(b, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace('（','(').replace('）',')')
            b_set.add(line)
    return b_set-a_set

# 计算两个字典（stat_dict2相对于stat_dict）value的增量，value为数值类型
def increment_for_dict(stat_dict, stat_dict2):    
    keys = stat_dict.keys()|stat_dict2.keys()
    increment_dict = dict()
    for x in keys:
        count = 0
        if x in stat_dict:
            count = stat_dict[x]
        count2 = 0
        if x in stat_dict2:
            count2 = stat_dict2[x]
        increment = count2 - count
        if increment!=0:
            increment_dict[x] = increment
    # increment_list= sorted(increment_dict.items(),key=lambda d:d[1], reverse=True)
    return increment_dict


# 合并文件内容，
# simplify, True表示使用文件名，Flase表示使用文件全路径
def merge_files(base_path, output_path, simplify, file_filter, line_filter):
    file_paths = get_files(base_path, file_filter)
    output_file = open(output_path, mode='w', encoding='utf-8')
    for file_path in file_paths:
        if simplify:
            file_name = os.path.basename(file_path)
        else:
            file_name = os.path.abspath(file_path)
        if not file_filter(file_name):
            continue
        with open(file_path, mode='r', encoding='utf-8') as f:
            for x in f:
                if not line_filter(x):
                    continue
                output_file.write('{}\t{}'.format(file_name, x))
    output_file.close()
    
if __name__ == '__main__':
    files = get_files('../')
    for f in files:
        print(f)
    print('------------------------------')
    dirs = get_dirs('../')
    for f in dirs:
        print(f)

    print(get_last_line('date_util.py'))
    print(get_last_not_blank_line('date_util.py'))
    print(get_line_count('file_util.py'))

    
    

