"""
1.什么是模块?有什么用?
    模块:就是一个python文件(.py)，其中就包含了变量、函数、类，以及可执行的代码。
    作用:提高代码复用性，降低开发门槛
2.导入模块的常用语法?(导入模块的语句，一般写在py文件的开头)
    import 模块名[as 别名]
    from 模块名import功能名[as别名]
    from 模块名 import *
"""

# 1.导入模块 import... --->调用方式：模块名.功能名 / 别名.功能名

# import random
# import random as rd

# 2.导入功能  form... import... --->调用方式：功能名 / 别名

# from random import randint
# from random import randint as rd

# for i in range(100):
#     print(rd.randint(1, 100))



from random import *

for i in range(100):
    print(randint(1, 100))

