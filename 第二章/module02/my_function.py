# __all__ 指定 from...import * 导入的是哪些功能
__all__ = ["PI","log_separator1", "log_separator2", "log_separator3", "log_separator4"]

# 常量（不会发生变化的数据 ；常量的名称需要全大写 ）
PI = 3.1415926
NAME = "社会你董哥NB666"

# 函数
def log_separator1():
    print("_ " * 30)    # “_” 重复输出30遍

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)


# 测试函数
# __name__ : Python中的内置变量，表示当前变量的名字
# （直接运行当前模块：__name__ 的值为“__main__”；）
# （当该模块被导入时：__name__ 的值为“模块名”）
# 执行当前文件，则会执行当前代码；如果该文件被当做模块导入则，以下代码不执行；
# 敲下 main 自动出现if执行代码
if __name__ == '__main__':
    log_separator1()