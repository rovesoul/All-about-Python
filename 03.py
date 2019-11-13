# -*- encoding: utf8 -*-
'''假如共享的资源有多个，多线程竞争时一般使用信号量（Semaphore）同步。信号量有一个初始值，表示当前可用的资源数，多线程执行过程中会通过 acquire() 和 release() 操作，动态的加减信号量。比如，有30个工人都需要电锤，但是电锤总共只有5把。使用信号量（Semaphore）解决竞争的代码如下：
————————————————
版权声明：本文为CSDN博主「天元浪子」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xufive/article/details/102993666'''
import time
import threading

S = threading.Semaphore(5)  # 有5把电锤可供使用


def us_hammer(id):
    """线程函数"""

    S.acquire()  # P操作，阻塞式请求电锤，
    time.sleep(0.3)
    print('%d号刚刚用完电锤' % id)
    S.release()  # V操作，释放资源（信号量加1）


def demo():
    threads = list()
    for i in range(30):  # 有30名工人要求使用电锤
        threads.append(threading.Thread(target=us_hammer, args=(i,)))
        threads[-1].start()

    for t in threads:
        t.join()

    print('所有线程工作结束')


if __name__ == '__main__':
    demo()
