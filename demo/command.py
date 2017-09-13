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