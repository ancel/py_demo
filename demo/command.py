import subprocess
import sys


if __name__ == '__main__':
    command_s = sys.argv[1]
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