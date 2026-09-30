# 1.导入模块
# import utils.my_fun
# import utils.my_var
#
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator3()
# print(utils.my_var.PI)
# print(utils.my_var.NAME)

# from utils import my_var
# from utils import my_fun
"""
注意:在通过 from utils import * 导入全部模块的时候，需要在-init__·py 文件中添加__all__=[]'，控制允许导入的模块列表。
"""
# from utils import *  # 导入包里的所有模块
#
# my_fun.log_separator1()
# my_fun.log_separator2()
# print(my_var.PI)
# print(my_var.NAME)



# 2.导入模块中的功能
# 相对路径：从当前文件所在目录开始查找
from utils.my_var import PI,NAME

# 绝对路径：从项目的根目录开始查找
# from 第二章.utils.my_var import PI,NAME


print(PI)
print(NAME)


