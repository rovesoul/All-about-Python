import os

print(os.getcwd()  )# 查看当前路径 

print(os.listdir())  # 查看当前路径下的文件及文件夹 

print(os.path.join(os.getcwd(), 'pythonw.exe') ) # 拼接 pythonw.exe 文件的全路径文件名,这个比较有用

