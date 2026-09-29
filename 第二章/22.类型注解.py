"""
1.类型注解的写法?
    变量:数据类型(如 a:int)
2.常见类型的写法
    int, float, bool, str, None, list, set, tuple,dict,str int
3.为什么要使用类型注解，有什么好处呢?
    代码结构更清晰、代码逻辑更安全、易维护
    更准确的代码自动提示
    提前发现代码潜在问题
4.注意：
    如果对变量直接赋值、变量运算等场景，Python会自动进行类型推断
    Python是动态类型语言，添加的类型注解只是提示，并不是强制约束!!!

"""

# 变量定义 - 未指定类型注解 ---> 类型推断
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None
names: list[str | int] = ["A", "C", "E",100]
phones = {"13309091111","15209101902", "18809019201"}
options = {"count": 2,"total":10}
g0ods = ("手机", 6999,1)

names.append("x")
names.append(10010)
names.append(1001.11)
print(names)


#变量定义指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None
names2: list[str | int] = ["A", "C", "E"]
phones2: set[str | int] = {"13309091111","15209101902", "18809019201"}
options2: dict[str,int] = {"count": 2,"total":10}
g0ods2:tuple[str,int,int] = ("手机", 6999,1)


def circle_area_len(r: float) -> tuple[float,float]:
    return round(3.14 *r * r , 1),round(3.14 * 2 * r,1)

print(circle_area_len(8.5))


def calculate_cost(coupon: int=0,points: int=0,delivery: float=0,*args: tuple[str,float,int]) -> float:
    """
    根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
    :param args: 商品信息（商品名，价格，数量）
    :param coupon: 优惠券
    :param points: 积分
    :param delivery: 运费
    :return: 订单总金额
    """
     # 2.计算商品总金额
    total_goods_cost = sum([goods[1] * goods[2] for goods in args])
    total_cost = total_goods_cost
    # 3.优惠卷
    if  total_goods_cost >= 5000 and coupon <= total_goods_cost:
        total_cost = total_goods_cost - coupon
# 4.积分抵扣
    if total_goods_cost >= 5000:
        total_cost -= points // 100
# 5.加上运费
    total_cost += delivery
    return total_cost


cost = calculate_cost(1000,1000,9.9,('手机',666,1),('电脑',6999,1),('牙刷',200,0),)
print(cost)