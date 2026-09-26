"""
字典定义：
    字典名 = {key：value，key2：value2，key3：value3...}
调用字典：
    v =字典名{key1}
注意事项：
    1.value可以是任意值，而 key 必须是不可变类型（str，int,float）
    key不能为（list、set、dict）
    2.key不能重复，如果重复则后面的值覆盖掉前面的值
"""

# #  定义字典 key如果重复后面的值替代前面的值
# dict1 = {"王林":550,"李慕婉":650,"韩立":740,"王建国":600,"王林":450}
# print(dict1)
# print(type(dict1))
#
# # 修改
# dict1["王林"] = 688
# print(dict1)
#
# # key必须是不可变类型（str，int，float，tuple），不能是list、set、dict
# dict2 = {0:123,1:321,1.5:456,"2":789,(1,2):000}
# print(dict2)
#
# # 访问
# print(dict1["韩立"])
# dict1["韩立"] = "NB666"
# print(dict1["韩立"])
# v = dict2[0]
# print(v)



"""
1. 字典的常用操作？
    添加：字典[key] = value（key不存在，就会执行新增）
    删除：del 字典[key] / value = 字典.pop(key)
    修改：字典[key] = value（key存在，就会执行修改）
    查询：字典[key] / 字典.get(key)；字典.keys() / 字典.values() / 字典.items()

2. 字典的遍历？
    字典支持 for 循环遍历
    通过 keys()、values()、items() 进行循环遍历

3. 注意：    
    字典[key]：如果 key 不存在，程序会直接报错崩溃（KeyError）。
    字典.get(key)：如果 key 不存在，程序不会报错，而是返回 None（空值）。
    你还可以给它设个默认值，比如 字典.get(key, 0)，找不到就返回 0
"""


# #-------------------------字典-常见方法-------------------------
#
# dict1 = {"王琳":677,"李慕婉":608,"徐立国":508,"韩立":550,"董哥":750}
# print(dict1)
# # 增加
# dict1["董大哥"] = 749
# print(dict1)
#
# # 删除
# v = dict1.pop("董大哥")
# print(v)
# print(dict1)
#
# del dict1["王琳"]
# print(dict1)
#
# # 修改
# dict1["徐立国"] = 620
# print(dict1)
#
# dict1["韩立"] = 668
# print(dict1)
# # 查询
#
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# print(dict1['董哥'])
# print(dict1.get('董大哥'))
#
# # 遍历
#
# for k  in dict1.keys():
#     print(f"{k}:{dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]}:{item[1]}")
#
# for k,v in dict1.items():
#     print(f"{k}:{v}")


"""
多行列操作：alt + shift
"""
# 案例 完成如下需求
#
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
#
# 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5.退出购物车

# 添加的数据结构：
# shopping_cart = {“name”：{“prince”：XX，“num”：2}，}

# 1.输出购物车车管理系统，询问客户操作

# 2.接受用户输入


# 3.根据客户输入的数字执行相应操作（match case）（增删改查、退出）

shopping_cart = {}
print('欢迎使用购物车系统！')
while True:
    print("""
    ################ 购物车管理系统 ##################   
    #                1.添加购物车                   # 
    #                2.修改购物车                   # 
    #                3.删除购物车                   # 
    #                4.查询购物车                   # 
    #                5.退出购物车                   # 
    ################ 购物车管理系统 ##################""")

    option = input("请选择要执行的操作（1-5）:")

    match option:
        case "1" : #添加购物车
            name = input('请输入要添加的商品名称：')
            if name not in shopping_cart:
                price = float(input('请输入商品价格：'))
                num = int(input('请输入商品数量：'))
                shopping_cart[name] = {'商品价格:':price,'商品数量:':num}
                print('添加商品成功！')
            else:
                print("要添加的商品已存在")

        case "2" : #修改购物车
            name = input('请输入要修改的商品名称：')
            if name in shopping_cart:

                price = input('请输入的商品价格：')
                num = input('请输入商品数量：')
                shopping_cart[name] = {'商品价格:': price, '商品数量:': num}
                print('商品修改成功！')
            else:
                print("要修改的商品不存在！")

        case "3" : # 删除购物车
            name = input('请输入删除的商品名称：')
            if name in shopping_cart:
               del shopping_cart[name]
               print(f'删除{name}成功！\n最新列表如下：')
               for name in shopping_cart.keys():
                   gods_info = shopping_cart[name]
                   print(f"商品名称:{name} \t 商品价格:{gods_info['商品价格:']} \t 商品数量:{gods_info['商品数量:']}")
            else:
                print("要删除的商品不存在！")

        case "4" : #查询购物车
            for name in shopping_cart.keys():
                gods_info = shopping_cart[name]
                print(f"商品名称:{name} \t 商品价格:{gods_info['商品价格:']} \t 商品数量:{gods_info['商品数量:']}")

        case "5" :
            print('退出购物车，bye~')
            break
        case _ :
            print('您的操作有误!')
            print()


