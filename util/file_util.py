import os
import subprocess
import threading


LOCK = threading.RLock()

def get_files(path): 
    assert os.path.isdir(path), '%s not exist.' % path 
    ret = [] 
    for root, dirs, files in os.walk(path): 
        for fn in files: 
            ret.append(os.path.join(root,fn)) 
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
