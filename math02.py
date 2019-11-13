'''三角函数相关'''
import math


a= math.sin(math.pi/2)      # 返回正弦值

b= math.cos(math.pi)        # 返回余弦值

c= math.tan(2/math.pi)      # 返回正切值

print(a)
print(b)
print(c)
print('')
# 弦值求弧度
a = math.acos(-1)       # 返回反余弦弧度值
3.141592653589793
b = math.asin(1)        # 返回反正弦弧度值
1.5707963267948966
c = math.atan(2)        # 返回反正切弧度值
1.1071487177940904
d = math.atan2(1, 3)    # 返回xy坐标值的反正切值
0.3217505543966422
print(a)
print(b)
print(c)
print(d)
print('')


#  弧度角度互转
print(math.degrees(math.pi/2),'度')
print(math.radians(180) ,'弧度')