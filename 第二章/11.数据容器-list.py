"""
数据容器---列表
    1.  定义： 列表名称 = [元素1，元素2，元素3]
        可以存放不同类型的元素，可重复、有序、元素可以修改
    2.列表的索引
        正向索引：从 0 开始
        反向索引：从 -1 开始
    3.列表的 删、改、查
        查看：list1[0]
        修改：list1[0] = ‘A’
        删除：del list1[0]
    注意：索引超出列表范围会报错
     print(s[10])
     IndexError: list index out of range
"""
# # #列表的定义、索引 正0、反-1
# s = [6,6,66,666,8,88,888,'A','B',True]
# # 列表类型
# print(type(s[1]))

# print(s)
# print(s[6])
# print(s[-1])
# print(s[3],s[6],s[7],s[-3],s[-4],s[-7])

# # 列表的修改、删除
# s[1] = False
# s[-1] = 'C'
# print(s)
#
# del s[1],s[1],s[3]
# print(s)
#
# # 遍历
# for item in s:
#     print(item,end=' ')


"""
 列表的切片：(左闭右开)
    s[start：end：step]  
    start：开始索引，不指定默认为0
    end：  索引结束位置，不指定默认为列表结尾
    step： 索引步长，不指定默认为1
"""

# # 定义列表
# list1 = ['a','b','c','d','e','f','g','h','i','j']
#
# # 切片操作 s[开始：结束：步长]
# # 切出来的也是列表
# print( list1[3:6:1])
# print(type(list1[3:6:1]))
# print( list1[3:6])
#
# print(list1[0:5:1])
# print( list1[:5:])
# print( list1[:5])
#
# print( list1[1:5:2])
# print( list1[1:-6:2])


"""
列表-常用方法
append（）    列表尾部追加元素
insert（a，b）    在a之前插入该元素b
remove（a）       删除列表中的第一个a
pop（）           删除列表中指定位置的索引，若未索引则删除最后一个
sort（）          对列表进行排序（列表中必须为同一种数据类型）
rever（）         反转列表元素
"""

# list1 = [16,18,19,56,0,1,2,666,888]
#
# # 列表尾部追加元素
# list1.append(566588)
# print(list1)
#
# # 插入元素
# list1.insert(7,3)
# print(list1)
# list1.insert(1,3)
# print(list1)
#
# # 删除
# list1.remove(3)
# print(list1)
#
# # 删除指定位置,默认删除最后
# n = list1.pop(2)
# print(n)
# print(list1)
#
# n1 = list1.pop()
# print(n1)
# print(list1)
#
# # 列表排顺序
# list1.sort()
# print(list1)
#
# # 反转列表元素
# list1.reverse()
# print(list1)



# # - - - >列表 list 案例< - - -
# # 案例1： 将用户输入的10个数字，存储在一个列表中，并将列表中的数字进行排序，输出其中的最小值，最大值，平均值
# # min() max() sum() len()
#
# # 1.定义列表
# num_list = []
#
# # 2.接收用户数字,10次循环,存储在列表中
# for i in range(10):
#     num = int(input("请输入一个数字："))
#     num_list.append(num)
# print("列表是：",num_list)
#
# # 3.排序
# num_list.sort()
# print("排序后：",num_list)
#
# # 4.输出最大值最小值平均值
# print("该列表最小值是：",num_list[0])
# print("该列表最大值是：",num_list[-1])
# print("该列表平均值是：",sum(num_list) / len(num_list))


# 案例2：合并两个列表中的元素，并对合并的结果进行去重处理
"""
 快速合并列表：
    1.解包：list = [*list1,*list2]]
    2.相加：list = list1 + list2
 判断元素在不在列表用 in
"""

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [12,23,45,78,6,8,9,45,3,]
#
# # 1.合并列表
# # 遍历出来列表所有元素再加入另一个列表
# for num in list2:
#     list1.append(num)
# print("合并后的列表",list1)
#
# # 2.去重
# new_list = []
# for num in list1:
#     if num not in new_list:
#         new_list.append(num)
# print("列表去重",new_list)


# # # 案例2（简化1）：合并两个列表中的元素，并对合并的结果进行去重处理
#
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [12,23,45,78,6,8,9,45,3,]
#
# # 1.合并列表
# # 解包：将列表这一类容器中的元素解开成一个一个独立的元素
# # 组包：将多个值合并到一个容器
# list = [*list1,*list2]
# print("合并后列表",list)
#
# # 2.去重
# new_list = []
# for num in list:
#     if num not in new_list:
#         new_list.append(num)
# print("列表去重",new_list)


# # # 案例2（简化2）：合并两个列表中的元素，并对合并的结果进行去重处理
#
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [12,23,45,78,6,8,9,45,3,]
#
# # 1.合并列表
# # 直接相加
# list = list1 + list2
# print("合并后列表",list)
#
# # 2.去重
# new_list = []
# for num in list:
#     if num not in new_list:
#         new_list.append(num)
# print("列表去重",new_list)


# # 案例3： 生成 1 - 20 的平方列表 ---> range（1，21）
# # 方式一：用循环遍历，取出元素再存入列表
# list1 = []
# for i in range(1,21):
#     list1.append(i**2)
# print(list1)
#
# # 方式二：
'''
列表推导式---> 按照一定的规则快速生成一个列表 --> 
语法格式1：[要输入的值 for i in 列表/序列]     
语法格式2：[要输入的值 for i in 列表/序列 if条件判断语句]  # 如果if条件成立则将值导入新列表中
'''
# num_list = [i**2 for i in range(1,21)]
# print(num_list)
#
#
# # 案例4：从一个数字列表中提取所有的偶数，并计算其平方，组成一个新的列表
# num_list1 = [32,87,9,23,1,545,78,44,98,2,4,6,8,10]
# new_list = [num ** 2 for num in num_list1 if num % 2 ==0]
#
# print(new_list)


# # list ---练习1：将如下多个列表合成一个列表，并去除重复元素，排好序（升序）后输出控制台
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# # 合并1 列表相加
# new_list1 = list1 + list2 + list3
# print("合并后",new_list1)
#
# # # 合并2 解包
# # new_list2 = [*list1, *list2, *list3]
# # print(new_list2)
#
# # 去重
# fin_list =[]
# for s in new_list1:
#     if s not in fin_list:
#         fin_list.append(s)
# print("去重",fin_list)
#
# # 排序，升序，输出
#
# fin_list.sort()
# print("排序",fin_list)



# # 练习2： 将如下列表中能被 3 或 5 整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表
# list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# nun_list  = [n**2 for n in list4 if n % 3 == 0 or n % 5 == 0]
# print(nun_list)

# 练习3： 将如下列表中的正数提取出来，封装为一个新的列表
list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
num_list3 = [n for n in list5 if n > 0]
print(num_list3)