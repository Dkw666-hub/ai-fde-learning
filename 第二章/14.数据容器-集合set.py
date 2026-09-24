"""
 1.集合的特点：
    无无序、不可重复、可以修改（不要依赖显示顺序）
 2.集合的定义及常用操作：
    定义1：集合名 = {元素1，元素2，元素3...}
    定义2：集合名 = set（）  #空集合定义方法
    常用操作：
    add（..）         添加元素到集合中                                            s1.add(“A”)
    remove（..）      移除集合中的指定元素（若指定不存在则报错）                       s1.remov（“A”）
    pop（）           随机删除集合中的元素并返回                                    s1.pop()
    clear（）         清空集合                                                   s1.clear
    difference（）    求两个集合的差集（包含第一个集合但不包含第二个集合的元素）          s1.difference（s2）
    union（）         求取两个集合的交集                                           s1.union（s2）
    intersection（）  求取两个集合的并集                                           s1.intersection（s2）
"""


# # 集合 set ---》无序，不可重复!，可修改
# # 定义：
# s1 = {12,415,3,5,2,5,6,6,6,8,8,8,666,888}
#
# print(s1)
# print(type(s1))
#
# # 定义空集合
#
# s2 = set()
#
# print(s2)
# print(type(s2))

##定义出来是字典
# s3 = {}
# print(s3)
# print(type(s3))


# # 常见方法：
# s1 = {100,300,200,800,400,500,600,900,900,700}
# print(s1)
# print(type(s1))
#
# # add（..）         添加元素到集合中
# s1.add(1200)
# print(s1)
#
# # remove（..）      移除集合中的指定元素（若指定不存在则报错）
# s1.remove(1200)
# print(s1)
#
# # pop（）           随机删除集合中的元素并返回
# e = s1.pop()
# print(e)
# print(s1)
#
# #clear（）         清空集合
# s1.clear()
# print(s1)
#
# #   difference（）    求两个集合的差集（包含第一个集合但不包含第二个集合的元素）          s1.difference（s2）
# s2 = {'A','B','C','D','E','F'}
# s3 = {'D','E','F','X','Y','Z'}
#
# print(s2.difference(s3))
#  # A B C
# print(s3.difference(s2))
#  # X Y Z
#
# #     union（）         求取两个集合的并集集                                           s1.union（s2）
# print(s2.union(s3))  #ABCDEFXYZ
# print(s3.union(s2))
#
# #     intersection（）  求取两个集合的交集
# print(s2.intersection(s3)) # D E F
# print(s3.intersection(s2))


# 集合综合案例：
"""
根据提供的班级学生选课情况，完成以下操作：
    1.找出同时选修了法语和艺术的学生
    2.找出同时选修了四门课的学生
    3.找出选修了足球，但是没有选修篮球的学生
    4.统计每一个学生选课的课程数量
"""

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1.找出同时选修了法语和艺术的学生 #交集 & .intersection（..）
frar_set = french_set.intersection(art_set)
frar_set1 = french_set & art_set
print(frar_set)
print(frar_set1)

# 2.找出同时选修了四门课的学生 #交集 & .intersection（..）
all_set = football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)
all_set1 = football_set & basketball_set & french_set & art_set
print(all_set)
print(all_set1)

# 3.找出选修了足球，但是没有选修篮球的学生  #差集 .difference ，-
fb_set = football_set.difference(basketball_set)
fb_set1 = football_set - basketball_set
print(fb_set)
print(fb_set1)

# 4.统计每一个学生选课的课程数量
# 4.1统计出每个学生的名单 # 集合推导式
all_name_set = football_set | basketball_set | french_set | art_set

# 4.2统计出每个名单在课程中出现的次数
all_list = [*football_set,*basketball_set,*french_set,*art_set]
for s in all_list:
    print(f"{s}选修了{all_list.count(s)}门课程")

