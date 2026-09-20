"""
案例2：
猜数游戏：
1.系统随机生成一个随机数
2.用户根究提示猜数字，并将所猜数字输入系统
3.如果猜错，系统给出提示是猜大了还是猜小了，然后继续输入猜的数字
4.如果猜对，系统自动退出，游戏结束

# # #
import random          #导入随机数库
random.randint（a，b）  #生成从a到b的随机整数
"""

# import random
# random_num = random.randint(1, 100)
#
# while True:
#     # 1.接受用户输入数据
#     num = int(input('请输入你猜的数字：'))
#
#     # 2.比较
#     if num > random_num:
#         print('猜大了')
#     elif num < random_num:
#         print('猜小了')
#     else:
#         print('恭喜你，猜对了！\nNB666')
#         break #退出循环
# print('随机生成的数字是',random_num)



# # 练习1：将1-1000之间（含1000）所有的5的倍数的数字累加起来
#
#累加和计数
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print('1-1000中5的倍数相加等于：',total)

# total = 0
# for i in range(1, 1001):
#     if i % 5 == 0:
#         total += i
#
# print("1-1000 5的倍数数字之和: ", total)



# 练习2： 统计字符串“qwertgfvacxsertyhagagfdretwearea4rtygh45646846153416k51k569k46kdytkrkdkfufuycucucf”
#         有多少个a和k（5个a，7个k）

# str1 = 'qwertgfvacxsertyhagagfdretwearea4rtygh45646846153416k51k569k46kdytkrkdkfufuycucucf'
# a = 0
# k = 0
# for i in str1:
#     if i == 'a':
#         a += 1
#     elif i == 'k':
#         k += 1
# print('字符串中a和k的个数分别为：',a,k)