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


#-------------------------字典-常见方法-------------------------

dict1 = {"王琳":677,"李慕婉":608,"徐立国":508,"韩立":550,"董哥":750}
print(dict1)
# 增加
dict1["董大哥"] = 749
print(dict1)

# 删除
v = dict1.pop("董大哥")
print(v)
print(dict1)

del dict1["王琳"]
print(dict1)

# 修改
dict1["徐立国"] = 620
print(dict1)

dict1["韩立"] = 668
print(dict1)
# 查询

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1['董哥'])
print(dict1.get('董大哥'))

# 遍历

for k  in dict1.keys():
    print(f"{k}:{dict1[k]}")

for item in dict1.items():
    print(f"{item[0]}:{item[1]}")

for k,v in dict1.items():
    print(f"{k}:{v}")