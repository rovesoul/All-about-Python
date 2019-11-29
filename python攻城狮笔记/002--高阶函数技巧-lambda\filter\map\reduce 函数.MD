python攻城狮002--高阶函数技巧-lambda\filter\map\reduce 函数

# lambda 函数 の 理解
> 表达式,创建内嵌\简单匿名函数
(匿名:没有名称的函数)

## filter 函数
> 返回一个filter对象,其中包含对其执行函数时,结果为真的所有元素
- filter(func ,seq)
> `示例如下:`f(n) 函数时lambda函数的代替品,同样的结果,通过这个理解lambda函数
```python
def f(n):
    """ 判断给定的数是不是寄数 """
    return n % 2 != 0


def use_filer(l):
    """
    获取指定列表/元祖中的奇数
    :param l: list/tuple 要过滤的数据
    :return: 过滤好的奇数列表
    """
    rest = filter(lambda n: n % 2 != 0, l)
    # rest = filter(f, l)
    return rest


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    rest = use_filer(l)
    print(list(rest))
		
# [1, 3, 5, 7, 9, 11]
```

## map函数
> 创建一个列表,其中包含对指定序列包含的项执行指定函数返回的值
- map(function,sequence,...)
> `示例如下:` 给一个列表,返回立方根. 通过三种方式演示,理解`lambda`,`map`两种函数的使用
```python

def pow_number(l):
    """
    根据给定的列表数据，计算里面每一项的立方
    :param l: list/type int类型的列表或者是元祖
    :return: 原来列表中每一项的立方
    """
    rest_list = []
    for x in l:
        rest_list.append(x * x * x)
    return rest_list

#------------------------------map函数示例
def f(n):
    """ 求给定数的立方 """
    return n * n * n


def pow_num_use_map(l):
    """
    使用map函数计算给定列表的每一项的立方
    :param l: list/type int类型的列表或者是元祖
    :return: 原来列表中每一项的立方
    """
    return map(f, l)
#------------------------------改造上个函数

def pow_num_use_lambda(l):
    """
    使用map函数\lambda表达式计算给定列表的每一项的立方
    :param l: list/type int类型的列表或者是元祖
    :return: 原来列表中每一项的立方
    """
    return map(lambda n: n * n * n, l)
#------------------------------

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 9]
    rest = pow_number(l)
    print(rest)
    print('-----------------')
    rest_map = pow_num_use_map(l)
    print(list(rest_map))
    print('-------------------')
    rest_lambda = pow_num_use_lambda(l)
    print(list(rest_lambda))

# pow_number打印结果 :  [1, 8, 27, 64, 125, 216, 343, 729]
# pow_num_use_map(l)打印结果 :  [1, 8, 27, 64, 125, 216, 343, 729]
# pow_num_use_lambda(l)打印结果 :  [1, 8, 27, 64, 125, 216, 343, 729]
```
## reduce函数使用
> 使用指定的函数,将序列的前两个元素合二为一,再将结果与第三个元素合二为一,以此类推,直到处理完整个序列并得到一个结果

- reduce(func, seq[,initial]
- 等价于 func(func(func(seq[0],seq[1]),seq[2]),...)
> `示例如下:` 
```python
from functools import reduce

#------------------------------ 循环求和
def get_sum(l):
    """
    根据给定的列表，求里面各个数字的总和
    :param l: list/type 里面是整数
    :return: 列表所有项的和
    """
    rest = 0
    for i in l:
        rest += i
    return rest
#------------------------------sum求和

def get_sum_use_py(l):
    """
    使用python内置的sum()进行求和
    :param l:
    :return:
    """
    return sum(l)

#------------------------------reduce求和
def f(m, n):
    """ 求两个数的和 """
    return m + n


def get_sum_use_reduce(l):
    """
    使用reduce进行求和
    :param l:
    :return:
    """
    return reduce(f, l)

#-----------------------reduce+lambda求和
def get_sum_use_lambda(l):
    """
    使用reduce + lambda进行求和
    :param l:
    :return:
    """
    return reduce(lambda m, n: m + n, l)


if __name__ == '__main__':
    l = [1, 2, 4, 6, 7, 8, 9]
    rest = get_sum(l)
    print(rest)
    print('--------------')
    rest_py = get_sum_use_py(l)
    print(rest_py)
    print('---------------')
    rest_reduce = get_sum_use_reduce(l)
    print(rest_reduce)
    print('------------')
    rest_lambda = get_sum_use_lambda(l)
    print(rest_lambda)

# 结果都是37
```
