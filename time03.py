import time
print(time.localtime() ) # 将时间戳转换为本地时区的struct_time 类。不提供时间戳，则使用当前时间戳

print(time.gmtime())  # 将时间戳转换为零时区的struct_time 类。不提供时间戳，则使用当前时间戳

print(time.localtime(0) ) # 0时间戳，对应我们东八区，就是1970年1月1日8时

print(time.gmtime(0))  # 0时间戳，对应格林尼治零时区，就是1970年1月1日0时

print(time.mktime(time.localtime()))  # struct_time 类转时间戳

print(time.localtime())
print(time.asctime())  # Wed Nov 13 23:31:38 2019
print(time.asctime((2019,10,1,12,30,30,0,0,0)))  # 将元组转化为时间戳

print(time.process_time()) #cpu 使用时长