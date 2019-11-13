import random  ,time
start = time.time()  # 记录启动时间
time.sleep(random.random())  # 在[0,1)秒中范围内随机休眠，模拟代码的运行
end = time.monotonic()  # 记录结束时间
print(end - start)  # 打印代码的运行时长


def timer():
    start =time.time()
    time.sleep(random.random())
    end= time.time()
    print(end-start)

timer()

timer()