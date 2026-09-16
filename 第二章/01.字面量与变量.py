# 字面量：直接书写的固定值（数据）
# #字面量的写法
# print(100) #整数（int） 
# print(3.14) #小数/浮点数（float）
# print(True) #布尔值
# print(False)
# print(None) #空值
# print("Python666")
# print("-----------")
# print(True-1)#布尔值True可以当数字1，False为0
# print(False+1)



# #变量：用来存储单个数据的容器，通常把发生变化的数据存储在变量中
# #Python是动态类型语言，一个变量可以存储不同类型数据，但通常存储一个类型的
# #格式：变量名 = 变量的值
# num = 123.1
# print(num)

# num = 666
# print(num)

# num = num + 1.1
# print(num)

# num = "加油"
# print(num)

# num = True
# print(num)

# num = None
# print(num)



# #案例：基础20.7，每月新增50，求未来两个月的总量
# base = 20.7     #基础播放量
# increase = 50   #新增播放量
# print("未来第一个月播放量：" , base + increase)
# print("未来第两个月个月播放量：" , base + increase + increase)

# #案例-一次性可以定义多个变量
# base,increase = 20.7,50
# print("未来第一个月播放量：" , base + increase)
# print("未来第两个月个月播放量：" , base + increase + increase)



#标识符：变量、函数、类等元素的名字
 #命名规则：
#1.只包含 “字母”、“数字”、“_”
#2.不能以数字开头
#3.不能以关键字命名
#4.严格区分大小写
 #命名规范：
#1.见名知意
#2.多个部分中间要加“_”
#2.英文字母全小写



# #案例：有两个变量a = 10，b = 20，现将两个变量值交换然后输出控制台
# a = 10
# b = 20
# c = a #c=10
# a = b #a=20
# b = c #b=10
# print(a,b)

# 练习：现有三个变量，分别为a = 100,b = 200,c = 300，现在将这三个变量
# a = 100，b = 200，c = 300，
# 分别赋值给c，a，b，并将其输出控制台
a,b,c = 100,200,300
temp = a
a = b
b = c
c = temp
print(a,b,c)


