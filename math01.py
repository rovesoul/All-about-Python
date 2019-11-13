import math
print ( math.ceil(4.1))  # 不考虑代价向上取整
print ( math.floor(4.1)) # 不考虑代价向下取整
print ( math.trunc(3.1415926))  #取整


# 四舍五入
print( round(3.5847))    #精确到个位
print( round(3.5847 , 2))  #保留两位
print(round(3.5847, 3))   #保留三位


# abs()返回的依据数据类型定
# math.fabs() 返回浮点型

print(abs(-5.7))  #内置abs,依据内容判断int还是flot
print(abs(-5))
print(math.fabs(-5.7)) #math的abs,均为浮点
print(math.fabs(-5))

# 乘方开方
print(pow(5,2))   #5的2次方
print(pow(5, 0.5))  # 5的0.5次方  即5的开方
print(math.pow(5, 2))  # 5的2次方
print(math.pow(5, 0.5))  # 5的0.5次方  即5的开方
print(math.sqrt(5))   # 5的开方



print(math.gcd(9, 6))  # 计算9和6的最大公约数(整数)

print(math.factorial(4) ) # 计算4的阶乘(整数)

print(math.fmod(17, 9))  # 计算A除以B的余数(浮点数)

print(math.ldexp(3, 10) ) # 结果为A乘以2的B次方(浮点数)


# 常量
print(math.pi)
print(math.e)
print(math.nan)
print(math.exp(2))# e的n次方
print(math.expm1(2))  # e的n次方-1
'''
其他内容见:
https: // blog.csdn.net/xufive/article/details/102993066?column = 9506563
'''
