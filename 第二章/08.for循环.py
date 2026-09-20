'''
for循环结构：

for 元素 in 待处理元素集
    循环代码体（对元素进行处理）

else：                #可选
    循环结束时，执行代码

'''


'''
range语句： 生成指定规则的数字序列
1. range（end） ----> 获取一个从零开始到end结束的数字集（不包括end）
2. range（ start，end） ----> 获取一个从start开始到end结束的数字集（不包括end）
3. range（start，end，step） ----> 获取一个从零开始到end，步长为step的数字集（不包括end）

'''


# # for循环： 便利输入的字符串

# msg = input("请输入需要遍历的字符：")

# for s in msg :   # s表示遍历出来的字符
#     print("元素:",s )

# else :
#     print("遍历结束")



# # 案例1：计算 1-100之间的所有奇数之和

# total = 0
# for i in range(1,101) :
#     if i % 2 == 1 :
#         total += i

# print("1-100之间的所有奇数之和为：" ,total)

# # 案例一简化版
# total = 0
# for i in range(1,101,2) :  
#     total += i

# print("1-100之间的所有奇数之和为：" ,total)


# # 案例2：计算 100 - 500 之间所有三的倍数的数字之和
#
# total = 0
# for i in range(100,501) :
#     if i % 3 == 0 :
#         total += i
#
# print("100 - 500 之间所有三的倍数的数字之和为：" ,total)



'''
#for嵌套循环

for 元素 in 待处理数据集1：
    循环体代码1
    循环体代码2                ###外层循环     
    ...
    for 元素 in 待处理数据集2：
        循环体代码1
        循环体代码2            ###内层循环
        ...
'''

# # print(“*") :自带换行效果 ，每一次执行都会输出新的一行
# # print（“*” ， end= ” “）：end表示的是每一次输出以什么结束；默认\n，表示换行，
# #打印一个长度为m，宽度为n的长方形
#
# m = int(input("请输入长方形的长："))
# n = int(input("请输入长方形的宽："))
#
# for i in range(n):
#     for j in range(m):
#         print("*", end="\t")
#
#     print()



# # 案例 ：打印九九乘法表
# #1.判断外层循环，内层循环控制什么
# #   外层：行数 内层：列数
#
# for i in range(1,10): #外层循环 - 控制行
#     for j in range(1,i+1): #内层循环 - 控制列
#         print(f"{j} X {i} = {i * j}",end="\t")
#     print()



# # 练习1：根据输入的直角边的边长，打印等腰直角三角形
# side = int(input("请输入直角边的边长："))
# for i in range(1,side + 1):
#     for j in range(i):
#         print("*",end="  ")
#     print()



# # 练习2：根据输入的数字，打印对应的数字金字塔
# # 分析：
# # 1.接受用户输入数字
# # 2.两层嵌套，外层打印行，内层打印列。打印格式为1 - n
# # 3.打印的时候加上数字
#
# n = int(input("请输入数字："))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="  ")
#     print()


# # 练习3：打印国际象棋棋盘
# # 格式 ■ □ ， 8 X 8的棋盘 ，交替输出黑白，输出八个在换行 两层嵌套循环
# for i in range(1,9):
#     if i % 2 != 0:
#         for j in range(4):
#             print("■  □",end="  ")
#         print()
#     else:
#         for j in range(4):
#             print("□  ■", end="  ")
#         print()

# # # 练习3代码块 模版
'''
行 + 列 数相加等于偶数为黑 等于奇数为白
'''
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end="  ")
        else:
            print("□", end="  ")
    print()

