import random

# for i in range(0, 10):
#     # random() 获取0到1的随机数，不包含0和1，返回浮点值
#     # print(random.random())
#
#     #获取随机整数，在指定范围内，包换开始和结束
#     # print(random.randint(1,9))
#
#     #获取指定区间之间的值，可以指定间隔值,包含开始，不包含结束
#     # print(random.randrange(1,9,2))
#
#     #随机获取列表中的元素,列表不能为空
#     print(random.choice([1, 3, 5, 7, 9, "a"]))
#     # print(random.choice([]))
# a = random.choice([1, 3, 5, 7, 9])
# print(a)
# print(type(a))

l = ["a", "b", "c", 1]
for i in range(len(l)):
    print(l[i])