import os
print(os.name)

# 获取PYTHONPATH环境变量的值
print(os.getenv('PYTHONPATH'))

# 返回当前系统的登录用户名
print(os.getlogin())

# 获取当前进程ID
print(os.getpid())

# 获取当前进程的父进程ID
print(os.getppid())

# 返回当前系统的CPU数量
print(os.cpu_count())

# 返回路径分隔符
print(os.sep)

# 返回当前系统的路径分隔符
print(os.pathsep)

# 运行平台上的cmd命令
os.system('cmd')

# 使用Excel打开D:\abc.xls文件
os.startfile('D:\\abc.xls')

# root->根目录，dirs->当前目录下所有的文件夹列表，files->当前目录下所有的文件列表
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
