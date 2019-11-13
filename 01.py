import time
import threading
'''我们设计一个任务：你（主线程）启动4个子线程，名字分别是A、B、C、D。
其中A线程启动后，你要先观察5秒钟，再启动其他线程。
每个子线程的任务是每隔指定时间间隔就向你问好，并报上自己的名字，你呢，只管睡觉。
30秒后，你醒了。你逐一检查了各个子线程的工作状态之后，结束运行。下面是实现代码：

但是，运行这段代码，你会发，当你喊下班的时候，小C并没有立刻撂下手头的活儿跟你走人，
而是做完了工作之后才跟你走人——或者说，是你在等他做完工作后一起走人。这里容易产生误会，
以为主线程结束后，子线程还会工作到任务完成。这是错误的理解。真相是，主线程不忍心打断正在忙碌的子线程（active），
一旦该子线程休眠（inactive），不管任务是否结束，都会被主线程直接带走。
————————————————
'''

def hello(name, t):
    """线程函数"""
    
    for i in range(10):
        print('Hello, 我是小%s'%name)
        time.sleep(t)

def demo():
    A = threading.Thread(target=hello, args=('A',1), name='A')
    B = threading.Thread(target=hello, args=('B',2), name='B')
    C = threading.Thread(target=hello, args=('C',3), name='C')
    
    #C.setDaemon(True) # 设置子线程在主线程结束时是否无条件跟随主线程一起退出
    
    A.start()
    A.join(5) # 等待A线程结束，若5秒钟后未结束,则代码继续
    B.start()
    C.start()
    
    time.sleep(20)
    
    print('进程A%s'%('还在工作中' if A.isAlive() else '已经结束工作',))
    print('进程B%s'%('还在工作中' if B.isAlive() else '已经结束工作',))
    print('进程C%s'%('还在工作中' if C.isAlive() else '已经结束工作',))
    
    print('下班了。。。')

if __name__ == '__main__':
    demo()
