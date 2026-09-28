"""
1.什么是局部变量，全局变量?
    在函数内部定义的变量就是局部变量，函数外声明的变量是全局变量。
2.global关键字的作用?
    在函数内部使用，声明接下来要使用的是全局变量，语法:global xxx
3.注意事项
    尽量避免在函数中使用全局变量，因为会使代码难以维护和调试
    考虑使用函数参数和返回值来传递数据，而不是依赖全局变量
    global主要用在程序的状态、配置和计数器等场景中
"""

# #------------------------- 函数 - 变量的作用域 ----------------------------------
# # # 全局变量：在函数外部 或 函数内部可以访问
#
# num = 100
#
# # 定义函数
# # 函数1：计算圆的面积 -- 半径
# def circle_area(r):
#     """
#     根据圆的半径 r 计算圆的面积
#     :param r: 半径
#     :return: 圆的面积（两位小数）
#     """
#
#     # 局部变量：只能在函数内部使用
#     global num  # global声明全局变量
#     num = 1000
#     pi = 3.14159
#     area = pi * r**2
#
#     print(num)  # 输出全局变量 num = 1000
#     return round(area, 2)
#
# print(circle_area(10))
# print(num)  # 输出全局变量 num = 1000

"""
1.位置参数
    调用函数时，传入的实参的顺序与定义函数时形参的顺序完全一致。
    
2.关键字参数
    调用函数时，通过"形参名=值"的形式传递参数，顺序没有要求。
    如果同时存在位置参数与关键字参数，位置参数在前，关键字参数在后。
3.两种传参方式的适用场景
    一切以代码结构清晰明了(可读性)、便于维护(维护性)为目标。
    如果参数比较少(不超过3个)，可直接使用位置参数。
    如果参数数量较多，建议使用关键字参数。
"""

# # ------------------------- 函数 - 传参方式 ----------------------------------
# # 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功,姓名:{name} , 年龄:{age} , 性别:{gender} , 城市:{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 方式一：位置参数
# stu = reg_stu('董哥',20,'男','河南')
# print(stu)
#
# # 方式二：关键字参数（不用按顺序）
# stu = reg_stu(name = '韩立',age =19 ,gender = '男',city = '中州')
# print(stu)
#
# stu = reg_stu(city = '天武大陆',age =999 ,gender = '女',name = '女帝')
# print(stu)
#
# #方式三：位置参数  +  关键字参数 ---> 必须！ 位置参数在前，关键字参数在后
# stu = reg_stu('厉飞雨',24 ,city = '西域',gender = '男')
# print(stu)

"""
 默认参数
    默认参数也称为缺省参数，用于在定义函数时，为参数提供默认值，调用函数时，可以不传递有默认值的参数。
    注意:默认参数必须放在没有默认值的参数列表的后面，一个函数在定义时是可以设置多个默认参数的。
    注意:函数调用时，如果为默认参数传递了值，则会修改默认的参数值;如果没有传递该参数，则直接使用默认值。
"""

# # ------------------------- 函数 - 默认参数 ----------------------------------
# # 定义函数
# def reg_stu(name, age, gender = '男', city = '河南'):
#     print(f"注册成功,姓名:{name} , 年龄:{age} , 性别:{gender} , 城市:{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 调用函数
# stu = reg_stu('张三',26)
# print(stu)
#
# stu = reg_stu('徐姐',18 , '女')
# print(stu)
#
# stu = reg_stu('徐姐',20 , '女','北京')
# print(stu)



# # ------------------------- 函数 - 不定长参数（位置参数 *args ---> 元组） ----------------------------------
# # 需求：根据实际传入的数据，计算这些数据的最大值、最小值、平均值
# def calculate_data (*args):
#     max_data = max(args)
#     min_data = min(args)
#     avg_data = sum(args)/len(args)
#     return max_data, min_data, round(avg_data, 2)
#
# data =  calculate_data(1,2,3,4,5,66,78,45,32,0)
# print(data)



# ------------------------- 函数 - 不定长参数（关键字参数 **kwargs ---> 字典） ----------------------------------
# 需求：根据实际传入的数据，计算这些数据的最大值、最小值、平均值
def calculate_data (*args,**kwargs):
    """
    根据实际传入的数据，计算这些数据的最大值、最小值、平均值
    :param args: 不定长位置参数，数据
    :param kwargs: 不定长关键字参数，选项
    :round:平均值小数位数
    :print: 是否打印
    :return: 最大值、最小值、平均值
    """
    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args)/len(args)
    print(args)
    print(kwargs)
    if kwargs.get('round')  is not None:
        avg_data = round(avg_data,kwargs.get('round'))
    if kwargs.get("print"):
        print(f"最大值：{max_data}  最小值：{min_data} 平均值：{avg_data} （保留{kwargs.get('round')}位小数）")
    return max_data, min_data, avg_data


# 调用函数                    *args: 不定长位置参数，数据       **kwargs: 不定长关键字参数，选项
data =  calculate_data(1,2,3,4,5,66,78,45,32,0,666,888,round = 2,print = True)
print(data)