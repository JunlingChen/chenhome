import math
'''
# print(math)
print(math.ceil(5.11))
print(math.floor(5.11))

#
# import keyword
# print(keyword.kwlist)
#四舍五入，返回整形
print(round(5.49))
print(round(5.51))

#开平方返回浮点值
print(math.sqrt(4.01))
print(math.sqrt(4.))
print(math.sqrt(4))

#幂运算，第一个数为底数，第二个数为指数，返回浮点型
print(math.pow(4,2))

#获取一个数的绝对值，返回为浮点数
print(math.fabs(5.4))
print(math.fabs(-5.4))
print(math.fabs(5))

# 获取绝对值，python自带函数，返回值由本身类型而定
print(abs(5.4))
print(abs(-5.4))
print(abs(5))

#函数运算结果id与原值不同
a = 5.4
print(id(a))
print(id(math.fabs(a)))

# 求和，python自带函数，返回值由本身类型而定
print(sum([1, 2, 3, 4.0]))
print(sum([1, 2, 3, 4]))

#求和，来自math模块，返回浮点值

print(math.fsum([1, 2, 3, 4]))

#math.modf() 讲一个浮点数拆分成整数部分和小数部分的元祖，小数在前，整数在后,返回元祖内值为浮点数
print(math.modf(5.4))
print(math.modf(5.0))
print(math.modf(5))
print(math.modf(0))
print(math.modf(0.5))
'''

#math.copysign() 将第二个数的符号（正负号）传给第一个数,返回浮点数字
print(math.copysign(3,-3))