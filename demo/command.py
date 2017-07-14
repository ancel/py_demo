import subprocess

# 执行命令
res = subprocess.Popen('tail -{} {}'.format(str(line_count),file_path),
    shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True) 
result = res.stdout.readlines() 
result2 = []
for x in result:
    result2.append(x.decode())