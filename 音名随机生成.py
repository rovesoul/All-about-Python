import random
a=int(input('输入你想生成多少个随机音名'))
b=[]
#for i in range(a)
for i in range(a):
    j= random.choice('ABCDEFG')
    # print(j)
    b.append(j)
# b=str(b)
print(b)