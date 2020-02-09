# 案例1
class Gizmo:
    def __init__(self):
        print('Gizmo id : %d' % id(self))

x=Gizmo()
y=Gizmo()

"""打印答案:
Gizmo id : 4303463440
Gizmo id : 4304340880
"""

# 案例2

charles = {'name': 'Charles L.Dodgson', 'bron': 1832, 'balance': 950}
lewis=charles
a= lewis is charles
print(a ) # True
print(id(lewis), id(charles))   # 4446862624 4446862624
print(lewis['bron']) # 1832

# 引入alex这个人的别名,姓名生日balance都一样
alex={'name':'Charles L.Dodgson','bron':1832,'balance':950}
b= alex==charles
print(b)  # True

c= alex is not charles
print(c)  # True

d = alex is charles
print(d)  # False


"""
==运算符比较两个对象的值(内部数据是否一样)
is 是在比较两个对象的标识是否一致,
通常我们关注值而不是标识,因此python中==出现频率高于is
"""
