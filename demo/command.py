import subprocess
import sys
import shlex



if __name__ == '__main__':
    command_s = sys.argv[1]

    # commanc_args = shlex.split(command_s)
    # res = subprocess.Popen(commanc_args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True) 
    # 执行命令
    res = subprocess.Popen(command_s,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True) 
    print(res.returncode)
    # res.communicate()
    print(res.wait())
    result = res.stdout.readlines() 
    for x in result:
        print(x.decode().strip())
    result = res.stderr.readlines() 
    for x in result:
        print(x.decode().strip())

    # 得到一个临时文件对象， 调用close后，此文件从磁盘删除
    out_temp = tempfile.SpooledTemporaryFile(max_size=10*1000)
    # 获取临时文件的文件号
    fileno = out_temp.fileno()
    res = subprocess.Popen(command_s,shell=True,stdout=fileno,stderr=fileno,close_fds=True) 
    return_code = res.wait()
    out_temp.seek(0)
    lines = out_temp.readlines()
    print(lines)
    out_temp.close()