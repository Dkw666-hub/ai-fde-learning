"""
if条件判断格式：
if 判断语句:
    执行语句

注意：1.条件判断的结果是布尔类型
     2.if条件后面要有：
     3.if里面的代码块有缩进（四个空格）表示归属关系
"""
# # if条件判断：如果分数大于680，我就去清华

# score = 700
# if score > 680:
#     print("清华大学欢迎你")
#     print("董柯炜NB666")



# ture_account = "188888888"
# ture_password = "666888"

# account = input("请输入您的账号：")
# password = input("请输入您的密码：")

# if account == ture_account and password == ture_password :
#     print("登陆成功！\n欢迎来到B站！")
# if account != ture_account or password != ture_password :
#     print("账号或密码错误")



"""
if...else结构：

if 判断条件：
    成立执行语句1
else：
    不成立执行语句2
"""

# # 案例：B站登录功能（正确账号密码为：188888888/666888）
# ture_account = "188888888"
# ture_password = "666888"

# account = input("请输入您的账号：")
# password = input("请输入您的密码：")

# if account == ture_account and password == ture_password :
#     print("登陆成功！\n欢迎来到B站！")
# else:
#     print("账号或密码错误")



"""# 案例： 根据用户输入的年份判断这一年是闰年还是平年。
     整百年份：必须能被400整除才是闰年
     非整百年份：能被4整除的年份是闰年
"""
# #程序:1.先让用户输入年份 2.判断年份是不是整百 3.判断闰年平年
# year = int(input("请输入年份："))
# if (year % 100 ==0 and year % 400  == 0) or year % 4 == 0 :
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")



# #练习1：根据用户输入的数字，判断该数字是奇数还是偶数。
# #1.接收用户数据 2.如果数字 % 2等于0则是偶数，否则为奇数
# num = int(input("请输入数字："))
# if (num % 2) == 0 :
#     print(f"{num}是偶数")
# else :
#     print(f"{num}是奇数")


# 练习2：根据用户输入的年龄，判断该用户是否成年（>=18）。
# year = int(input("请输入年龄："))
# if year >= 18 :
#     print(f"{year}岁，您已经成年")
# else :
#     print(f"{year}岁，你还未成年")


# #练习3：根据用户输入的数字，判断该数字是正数还是负数。
# num = int(input("请输入数字："))
# if num > 0 :
#     print(f"{num}是正数")
# elif num == 0:
#     print(f"{num}既不是正数也不是负数")
# else :
#     print(f"{num}是负数")


# #练习4：根据用户输入的考试分数，判断是否及格。(>=60)。
# score = int(input("请输入成绩："))
# if score >= 60 :
#     print(f"{score}分，合格")
# else :
#     print(f"{score}分，不合格")



"""
if...elif...else结构：

if 判断条件：
    成立执行语句1
elif 判断条件：
    成立执行语句2
else:
    都不成立执行语句3

注意：
1.elif可以写多个
2.else只能写一个，必须放最后
3.多个条件判断顺序从上到下中间有条件成立，就不再执行

"""


# # 案例：三角形类型判断：根据输入的三个边的边长（正整数），判定是等腰三角形、等边三角形、普通三角形还是不能构成三角形
# # 1.判断输入数据是否是正整数
# # 2.判断任意两边之和是否大于第三边
# # 3.如果是三角形的话判断三角形类型 等边 等腰 普通

# side1 = int(input("请输入三角形的第一个边长："))
# side2 = int(input("请输入三角形的第二个边长："))
# side3 = int(input("请输入三角形的第三个边长："))

# if side1 <= 0 or side2 <= 0 or side3 <= 0 :
#     print("请输入正确的边长")
# elif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1 :
#      if side1 == side2 ==side3 :
#           print("这个是等边三角形")
#      elif side1 == side2 or side1 == side3 or side2 ==side3 :
#           print("这个是等腰三角形")
#      else :
#           print("这个是普通三角形")
          
# else :
#      print("这不能构成三角形")



# 北京市居民年度用电电费计算：根据输入的用电度数，计算电费
# 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
# - 阶梯电价规则：
#   1. 第一档：2880度以下，电费单价0.4883元/度
#   2. 第二档：2880-4800度，电费单价0.5383元/度
#   3. 第三档：4800度以上，电费单价0.7883元/度
'''
1.接受用户输入数据
2.首先要判断电费在哪一个档位
3.计算这一档位电费，再加上上一个档位的上线电费
4.输出最终电费

'''
usage_elec = float(input("请输入用电度数："))
#定义电价
first_sprice = 0.4883
second_price = 0.5383
third_price  = 0.7883
#定义前两阶段用电上线
first_max = 2880
second_max = 4800

total_usage = 0.0

if usage_elec < first_max :
    total_usage = usage_elec * first_sprice
    
elif first_max <= usage_elec <= second_max :
    total_usage = (usage_elec -first_max) * second_max + first_max * first_sprice
    
else:
    total_usage = first_max * first_sprice + (second_max - first_max) * second_price + (usage_elec - second_max) * third_price

print(f"{usage_elec}度的电费是:{total_usage}元")
