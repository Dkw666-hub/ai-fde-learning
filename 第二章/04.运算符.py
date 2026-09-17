# # 算数运算符: + - * / // % **
# print("6 + 4 = ", 6 + 4) # 加 10
# print("6 - 4 = ", 6 - 4) # 减 2
# print("6 * 4 = ", 6 * 4) # 乘 24
# print("6 / 4 = ", 6 / 4) # 除 1.5（结果是小数）
# print("6 // 4 = ", 6 // 4) # 整除 1
# print("6 % 4 = ", 6 % 4) # 取余/求模 2
# print("6 ** 4 = ", 6 ** 4) # 幂指数 6的4次方 1696



# #算术运算的优先级 ---> () ---> ** ---> * / // % ---> + -
# print( 0.1 + 10 / 4 ** 2) # 10 / 16 + 0.1



# # 案例：输入两个数 x y ，计算 x + y 以及 x - y 的结果并输出
# # float(..) 将括号中的值转化为浮点数
# # 0000000000000009 --->精度损失：计算机基于二进制进行数据存储与处理，二进制无法准确表示所有的小数，可能会存在精度损失

# x = float(input("请输入x的值："))
# y = float(input("请输入y的值："))

# print(f"x + y = {x + y} \nx - y = {x -y}")



# # 练习1：计算三个整数的平均数
# int1 = int(input("请输入第一个整数"))
# int2 = int(input("请输入第二个整数"))
# int3 = int(input("请输入第三个整数"))
# print(f"这三个整数的平均值为：{ ( int1 + int2 + int3 ) / 3 }")


# # 练习2：要求输入梯形的上底，下底，高，计算梯形的面积
# upaside = float(input("请输入上底"))
# downaside = float(input("请输入下底"))
# high = float(input("请输入高"))
# print(f"梯形的面积为：{ (upaside + downaside) * high / 2}")


# # 练习3：要求输入圆的半径，然后计算圆的周长和面积
# r = float(input('请输入圆的半径'))
# pai = 3.1415926
# print(f'圆的周长是：{2 * r} \n圆的面积是：{pai * r * r}')


# # 练习4：身体质量指数BMI计算（BMI = 体重（kg）/ 身高（m）**2）
# # 1.输入体重(kg)
# # 2.输入身高（m）
# # 3.计算BMI并输出              
# weight = float(input("请输入体重（kg）："))
# high = float(input("请输入身高（m）："))
# print(f"您的BMI为{weight / high ** 2}")



# #  赋值运算符 ：= += -= *= /=  //= %= **=  
# num = 85

# num += 10 # num = num + 10
# print("num += 10后，num = ",num) # num = 95

# num -= 10 # num = num - 10
# print("num -= 10后，num = ",num) # num = 85

# num *= 10 # num = num * 10
# print("num *= 10后，num = ",num) # num = 850

# num /= 10 # num = num / 10
# print("num /= 10后，num = ",num) # num = 85.0

# num //= 10 # num = num // 10
# print("num //= 10后，num = ",num) # num = 8.0 

# num %= 10 # num = num % 10
# print("num %= 10后，num = ",num) # num = 8.0

# num **= 2 # num = num ** 2
# print("num **= 10后，num = ",num) # num = 64.0



# #  比较运算符：== !=  > >=  < <=   
# print("比较100 == 100的关系：",100 == 100) # True
# print("比较100 != 100的关系：",100 != 100) # False
# print("比较100 > 100的关系：",100 > 100) # False
# print("比较100 >= 100的关系：",100 >= 100) # Ture
# print("比较100 < 100的关系：",100 < 100) # False
# print("比较100 <= 100的关系：",100 <= 100) # Ture



# # 逻辑运算符: and or not
# # 案例一：键盘输入一个整数，判断这个整数是否是在 10 - 20 之间---> 在：Ture 不在：False
# num = int(input("请输入一个整数:"))
# print("这个数在10 - 20之间:",num >= 10 and num <= 20)


# # 案例二：判断这个数是否不在 10 - 20 之间
# num = int(input("请输入一个整数:"))
# print("这个数不在10 - 20之间:",num < 10 or num > 20)