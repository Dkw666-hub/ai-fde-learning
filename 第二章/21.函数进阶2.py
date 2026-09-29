"""
函数的参数类型:
    普通参数:数字、布尔、字符串、列表、元组、集合、字典等。
    特殊参数:函数。
    def calcu(x,y,oper)
    return oper（x，y）
    定义时加上 oper 代表调用函数
    calcu（x，y，oper）
"""
# # Addition, subtraction, multiplication, and division, calculation
# # 函数的参数类型
#
#
# # 加
# def addition(x,y):
#     return x + y
#
# # 减
# def subtraction(x,y):
#     return x - y
# # 乘
# def multiplication(x,y):
#     return x * y
#
# # 除
# def division(x,y):
#     return x / y
#
# # 计算
# def calculation(x,y,oper):
#     return oper(x,y)
#
# # 调用
# v =  calculation(10,20,addition)
# print(v)
#
# v = calculation(10,20,subtraction)
# print(v)
#
# v = calculation(10,20,multiplication)
# print(v)
#
# v = calculation(10,20,division)
# print(v)


"""
1.匿名函数的定义方式:
    lambda 参数列表:函数体

2.命名函数与匿名函数的选择?
    建议使用匿名函数的情况:函数逻辑简单，只在一个地方调用(常作为高阶函数的参数)
    建议使用命名函数的情况:函数逻辑复杂，需要多步操作，需要多个地方重复使用或需要加
    文档说明的场景
3.代码的可读性和可维护性比简洁性更重要
"""

# 定义分割线函数
# def out_lien():
#     print("----------------------------------------")
# out_lien()

# # 匿名函数
# out_line = lambda : print('--------------------------------------')
# out_line()
#
# # 定义加法函数
# # def add(x,y):
# #     return x+y
# # print(add(5,10))
#
# # 匿名函数
# add = lambda x,y : x + y
# print(add(10,20))

# # 需求3:完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序;
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# print(data_list)
# data_list.sort(key= lambda item : len(item) ) # 匿名函数的典型应用场景
#
# print(data_list)


# ------------------------------函数递归-案例-------------------------------------
# 案例一: 计算n的阶乘
# 递归调用（先层层递进，再逐层回归）：指的是在函数当中自己调用自己的情况 ---> 一定得有终结点
"""
n的阶乘公式：
f（n）= n * f（n-1）

jc(10) = 10 * jc(9)
jc(9) = 9 * jc(8)
jc(8) = 8 * jc(7)
jc(7) = 7 * jc(6)
jc(6) = 6 * jc(5) = ...
jc(5) = 5 * jc(4) = 5 * 24 = 120
jc(4) = 4 * jc(3) = 4 * 6 = 24
jc(3) = 3 * jc(2) = 3 * 2 = 6
jc(2) = 2 * jc(1) = 2 * 1 = 2
jc(1) = 1
函数递归计算过程，先下后上
"""

# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         jcv =  n * jc(n - 1)
#         return jcv
#
# print(jc(10))

# 案例 电商订单计算器
# 定义一个函数，用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
# 具体规则如下:优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100识分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)

# ('手机',3999,1),('电脑',6999,1),(...), ...
# 计算总价 = 商品总金额 - 优惠券 - 积分抵扣 + 运费

# # 1.传入商品信息，不定长参数接收
# # 传参方式一：
# def calcu_cost(coupon=0,points=0,delivery=0,*args):
#     """
#     根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
#     :param args: 商品信息（商品名，价格，数量）
#     :param coupon: 优惠券
#     :param points: 积分
#     :param delivery: 运费
#     :return: 订单总金额
#     """
#      # 2.计算商品总金额
#     total_goods_cost = sum([goods[1] * goods[2] for goods in args])
#     total_cost = total_goods_cost
#     # 3.优惠卷
#     if  total_goods_cost >= 5000 and coupon <= total_goods_cost:
#         total_cost = total_goods_cost - coupon
# # 4.积分抵扣
#     if total_goods_cost >= 5000:
#         total_cost -= points // 100
# # 5.加上运费
#     total_cost += delivery
#     return total_cost

# #不够5000
# # cost = calcu_cost(('手机',399,1),('电脑',699,1),('牙刷',2,10),coupon=100,points=1000,delivery=9.9)
# # print(cost)
#
# #够5000
# cost = calcu_cost(1000,1000,9.9,('手机',3999,1),('电脑',6999,1),('牙刷',200,10),)
# print(cost)


#传参方式二：
def calcu_cost(*args, **kwargs):
    """
    根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
    :param args: 商品信息
    :param kwargs: 传入 优惠券 coupon=,积分 points=,快递费 delivery=
    :return: 订单总金额
    """
     # 2.计算商品总金额
    total_goods_cost = sum([goods[1] * goods[2] for goods in args])
    total_cost = total_goods_cost
    # 3.优惠卷
    coupon = kwargs.get('coupon',0)
    if total_goods_cost >= 5000 and coupon <= total_goods_cost:
        total_cost = total_goods_cost - coupon
# 4.积分抵扣
    points = kwargs.get('points',0)
    if total_goods_cost >= 5000:
        total_cost -= points // 100
# 5.加上运费
    delivery = kwargs.get('delivery',0)
    total_cost += delivery
    return total_cost

cost = calcu_cost(('手机',3999,1),('电脑',6999,1),('牙刷',200,10),coupon=1000,points=1000,delivery=9.9)
print(cost)