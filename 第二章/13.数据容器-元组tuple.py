
"""
# 元组的基本操作：
 1.元组的特点：
    元素可以重复
    有序
    不可修改（只读）
 2.元组的两个查询方法
    count（） ：统计指定元素的数量
    index（） ：获取元素第一次出现的位置，若钙元素不存在则报错
 3.元组使用的注意事项
    定义单元组元素时，需在结尾加上，如：（‘A，’）
"""

#
# ### 元组的基本操作 - tuple ---》元素可以重复，有序，不可修改
# # 定义
# t1 = (5,6,6,43,2,345,66,666,888,'A','B')
#
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[1])
# print(t1[7])
#
# # 切片
# print(t1[6:9:1])
# print(t1[-3:-6:-1])
#
# # 元组的两个查询方法 count() ：计数  index() ：索引元素位置
# print(t1.count("A"))
# print(t1.count(6))
#
# print(t1.index("A"))
# print(t1.index(6))
#
#
# # 注意 定义单元素元组时，单个元素之后需要加上 ，比如 （100，）
#
# t2 = ()
# print(t2)
# print(type(t2))
#
# t3 = (66,)
# print(t3)
# print(type(t3))



'''
元组的组包与解包
 1.组包：将多个值合并到一个容器中（元组，列表）。
 2.解包：将容器中的元素分别赋值给多个变量。
    注意：在元组解包时 * 表示收集剩余所有元素，允许我们处理不确定数量的元素
'''

# 案例1： 有两个变量 a = 10 b = 20，将两个变量值交换，输出控制台

# a = 10
# b = 20
#
# # 组包：
# t1 = a,b
#
# # 解包：
# b,a = t1

# # 合并
# # a,b = b,a
# print(a,b)

# # 案例2： 有三个变量 a = 100，b = 200， c = 300，将这三个变量交换将abc分别赋值给 c a b输出控制台
# a = 100
# b = 200
# c = 300

# # 组包
# t2 = a, b, c
# print(t2)
#
# # 解包
# c,a,b = t2
# print(a,b,c)

# # 合并
# c,a,b = a,b,c
# print(a)
# print(b)
# print(c)



'''
 拓展解包：（* 收集剩余的所有元素，封装列表list中）
'''
# t1 = (88,1,2,3,5,9,7,89,56,23,12,45,66)
# t2 = 88,6,2,3,5,9,7,6,56,23,12,45,66
# print(t1)
# print(t2)
#
# # 拓展解包：* 收集剩余所有元素
# first,*other,last = t1
# print(first)
# print(other)
# print(last)
#
# *last3,last2,last1= t2
# print(last1)
# print(last2)
# print(last3)
#
# first1,first2,*other,last11 = t2
# print(first1)
# print(first2)
# print(other)
# print(last11)


''' {avg:.1f} ---> 保留一位小数
    快捷键：shift + tab 选中快速横移
    '''
# #元组综合案例： 根据提供的学生成绩单完成要求：
#     1.计算每个学生的总分，平均分，然后输出出来
#     2.统计各科成绩的最低分，最高分，平均分，并输出
#     3.查找成绩优秀（平均分大于90）的学生，并输出

students = (
    ('S001','王林',85,92,78),
    ('S002','李慕婉',92,88,95),
    ('S003','十三',78,85,82),
    ('S004','曾牛',88,79,91),
    ('S005','周易',95,96,89),
    ('S006','王卓',76,82,77),
    ('S007','红蝶',89,91,94),
    ('S008','徐立国',75,69,82),
    ('S009','许木',86,89,98),
    ('S0010','通天',66,59,72)
)

# 1.计算每个学生的总分，平均分，然后输出出来
# # 方式一：
# print("学号 \t\t 姓名 \t\t 语文 \t\t 数学 \t\t 英语 \t\t 总分 \t\t 平均分")
# for s in students: # ('S001','王林',85,92,78),
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t\t {s[1]} \t\t s[2] \t\t s[3] \t\t  s[4] \t\t {total} \t\t {avg:.1f}")

# 方式二：元组解包
print("学号 \t\t 姓名 \t\t 语文 \t\t 数学 \t\t 英语 \t\t 总分 \t\t 平均分")
for id,name,chiese,math,english in students: # ('S001','王林',85,92,78),
    total = chiese + math + english
    avg = total / 3
    print(f"{id} \t\t {name} \t\t {chiese} \t\t {math} \t\t {english} \t\t {total} \t\t {avg:.1f}")


# 2.统计各科成绩的最低分，最高分，平均分，并输出
# 2.1获取学生成绩列表
    chinese_scores = [s[2] for s in students]
    math_scores = [s[3] for s in students]
    english_scores = [s[4] for s in students]
print()
# 2.2输出各科最高分，最低分，平均分
print(f"语文最高分：{max(chinese_scores)}\t最低分:{min(chinese_scores)}\t平均分:{sum(chinese_scores) / len(chinese_scores):.1f}")
print(f"数学最高分：{max(math_scores)}\t最低分:{min(math_scores)}\t平均分:{sum(math_scores) / len(math_scores):.1f}")
print(f"英语最高分：{max(english_scores)}\t最低分:{min(english_scores)}\t平均分:{sum(english_scores) / len(english_scores):.1f}")


# 3.查找成绩优秀（平均分大于90）的学生，并输出
# # 方式一：
# print()
# print("成绩优秀名单如下：")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg >= 90:
#         print(f"学号:{s[0]} \t 姓名:{s[1]} \t 平均分:{avg:.1f}")


# 方式二：元组解包
print()
print("成绩优秀名单如下：")
for id,name,chiese,math,english in students:
    total = chiese + math + english
    avg = total / 3
    if avg >= 90:
        print(f"学号:{id} \t 姓名:{name} \t 平均分:{avg:.1f}")



