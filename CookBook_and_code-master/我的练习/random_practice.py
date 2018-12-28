import math
import random

num = input("请输入一个三位数的随机数 ")

l1 = list(range(65,91))
l2 = list(range(97,123))
l3 = l1 + l2
str_num = [[0 for i in range(12)] for j in range(10)]
str_new = ""
def random_str():
    for i in range(10):
        for j in range(4):
            global str_new
            str_new = str_new + str(chr(random.choice(l3)))
            # str_num[i][j] = str(chr(random.choice(l3)))
            # print(str_num[i][j])
            # print(chr(random.choice(l3)),end="")
        for k in range(4,12):
            str_new = str_new + str(random.randrange(0,10))
            # str_num[i][k] = random.randrange(0,10)
            # print(random.randrange(0,10),end="")
        # print(str_num[i])     #以列表的形式输出
        print(str_new)  #以字符串的形式输出
        with open("str_new.txt","a") as f:
            f.write(str_new+"\n")
        str_new = ""



if num.isdigit() and 100 <= int(num) <= 999:    #注意先判断是否为数字，在判断是否在范围内
    random_num = random.randrange(100,1000)
    _num = int(num)
    if _num > random_num:
        print("这个三位数的百位数是：",_num//100)
        print("这个三位数的十位数是：",_num//10%10)
        print("这个三位输的个位数是：",_num%100%10)
    elif _num ==random_num:
        print("恭喜您中大奖了！")
    else:
        print("输入的三位数小于随机数")
        random_str()


else:
    print("请输入符合规范的随机数")


