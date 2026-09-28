"""
1.函数定义及调用的语法?
 #函数的定义
    def out_line():
    print('-------------------')

 :函数的调用
    out_line()
2.函数使用的注意事项
    函数必须先定义，在调用
    函数定义时，并不会执行，只有在调用函数时，函数体的逻辑才会运行
    函数中通过缩进来描述归属关系

3.函数参数和返回值
    函数可以有多个返回值和参数，中间用 ， 隔开
    函数定义时 参数是形参，调用时为实参
    多个返回值为元组形式，可以解包
    round（值，小数位数）保留几位小数

4.函数的嵌套调用
    嵌套调用指的是在一个函数中，又调用了另外一个函数。
    函数调用遵循栈结构，最后被调用的函数最先返回LIFO(Last In First Out，后进先出)
"""

# # 定义函数
# def print_line():
#     print('------------------------')
#     print('------------------------')
#
# # 调用函数
# print_line()
# print_line()


# # 函数的参数与返回值
#
# # 函数1：计算圆的面积 -- 半径
# def circle_area(r):
#     """
#     根据圆的半径 r 计算圆的面积
#     :param r: 半径
#     :return: 圆的面积（两位小数）
#     """
#     cira = 3.14 * r**2
#     return round(cira, 2)
#
# ac = circle_area(10)
# print(circle_area(5))
# print(ac)
# print(type(ac))
#
# # 函数2：计算长方形的面积 -- 长，宽
# def Rectangle_area (l , w):
#     """
#     根据长方形的长，宽 计算长方形的面积
#     :param l:  长度
#     :param w:  宽度
#     :return:  长方形面积（1位小数）
#     """
#     return round(l * w,1)
#
# print(Rectangle_area(1.1,2))
# print(type(Rectangle_area(1.1,2)))
#
# # 函数3：计算圆的面积，周长 -- 半径
# def circle_area_len(r):
#     """
#     根据圆的半径 r 计算圆的面积
#     :param r: 半径
#     :return:  圆的面积，圆的周长
#     """
#     return round(3.14 * r**2 , 1),round(3.14 * 2 * r , 1)
#
# cl = circle_area_len(10)
# print(type(cl))
# print(cl)
#
# area,len = circle_area_len(10)
# print(area)
# print(len)



# 函数的嵌套调用

def function_a():
    print('a ...before')
    function_b()
    print('a ...after')

def function_b():
    print('b ...before')
    function_c()
    print('b ...after')

def function_c():
    print('c ...')

function_a()
print("嵌套函数调用成功~")