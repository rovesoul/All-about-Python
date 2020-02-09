"""装饰器将函数添加到空列表,并原封不动的返回函数本身,而在整体运行的时候哦可以看到,装饰器在调用main之前就运行了, 更进一步,在main调用后可以看到第二行打印的结果"""



registry=[]

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('register -> ', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()
