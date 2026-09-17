# # type() 获取指定字面量或变量（里面的数据）的类型
# print("hello world")
# print(type("hello world")) # str
# print(type(1234666)) #int
# print(type(3.14)) #float
# print(type(True)) #bool
# print(type(False)) #bool
# print(type(None)) #NoneType

# num = 5666
# print(type(num)) # int


# # isinstance（数据，类型）---> bool值---> 判定变量是否是指定的类型，如果是：返回True，否则：False
# print(isinstance(num,int)) # True
# print(isinstance(num,float)) # False
# print(isinstance(num,str)) # False



# # 字符串

# # 定义字符串的三种方式:' '," ",""" """ 
# # 单引号和双引号等效，项目中保持一种写法即可

# s1 = "Hello" # 双引号定义
# s2 = 'Python' # 单引号定义
# s3 = """
# Hello:
#     我们一起来学AI吧！
#     今天你敲代码了吗？
# """ #三引号定义（多行字符串）

# print(s1)
# print(s2)
# print(s3)

# print(type(s1))
# print(type(s2))
# print(type(s3))


# # 定义字符串---> It's very good
# # 转义字符 \' \" \n （换行） \t (制表Tab)

# msg = 'It\'s very good'
# print(msg)

# msg2 = "It's very good"
# print(msg2)

# msg3 = "Hello的意思就是:\"您好\""
# print(msg3)

# msg4 = 'Hello的意思就是:"您好"'
# print(msg4)

# print("Hello:\n\t我们一起来学AI吧！\n\t今天你敲代码了吗？")



# # 字符串拼接

# s1 = "人生苦短" " 我用Python" " , OK"
# print(s1)

# msg1 = "人生苦短"
# msg2 = "我用Python"
# print("龟叔说：" + msg1 + " , " + msg2 + ".")
# print("董哥说：" + msg1 + " , 及时行乐。")


# # 案例：---> str（int数字）---> 将int类型数字转化为字符串
# # 输出：大家好，我是XX，今年XX岁，学的专业是XX，爱好是XX

# name = "徐伊灿"
# age = 18
# profession = "电子信息工程"
# hobby = "睡觉，吃好吃的"
# print("大家好, 我是" + name + "，今年" + str(age) + "岁，学的专业是" + profession + "，爱好是" + hobby)


# # 字符串格式化 ---> 方式一：%s 占位符

# name = "徐伊灿"
# age = 18
# profession = "电子信息工程"
# hobby = "睡觉，吃好吃的"
# print("大家好, 我是%s,今年%s岁,学的专业是%s,爱好是%s" % (name,age,profession,hobby))

# print("我%s,年龄：%s,学的%s，爱好是：%s" % (name,age,profession,hobby))

# 字符串格式化 ---> 方式二：f"...{变量名/表达式}..."
# ---> 推荐方式

name = "徐伊灿"
age = 18
profession = "电子信息工程"
hobby = "睡觉，吃好吃的"
print(f"大家好，我是{name}，今年{age}岁，学的专业是{profession}，爱好是{hobby}")




